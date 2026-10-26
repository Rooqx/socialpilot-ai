#!/usr/bin/env python3
"""Local-only state manager for portable-social-agent. Python >=3.10; stdlib only.
No network clients, no posting, no DMs, no scheduler: stages files for HUMAN action.
"""
import argparse, contextlib, hashlib, json, math, os, re, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parent.parent
PLATFORMS={'x','instagram','linkedin'}
FORMATS={'post','thread','carousel','reel','story','document','image','video'}
PLATFORM_FORMATS={
    'x': {'post','thread','image','video'},
    'linkedin': {'post','document','carousel','image','video'},
    'instagram': {'post','carousel','reel','story','image'},
}
STAGES={'draft','needs_review','approved','manual_handoff','reported_published'}
SCHEMA=1

def now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def read(path,default=None):
    try: return json.loads(path.read_text(encoding='utf8'))
    except FileNotFoundError: return default

def atomic(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,name=tempfile.mkstemp(prefix='.tmp-',dir=str(path.parent))
    try:
        with os.fdopen(fd,'w',encoding='utf8') as f:
            json.dump(value,f,ensure_ascii=False,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
        os.replace(name,path)
    finally:
        if os.path.exists(name): os.unlink(name)

def fail(msg): raise ValueError(msg)

def load_state(base):
    s=read(base/'state.json')
    if not s: fail('Not initialized. Run: python3 scripts/socialctl.py init')
    if s.get('schema_version')!=SCHEMA: fail('Unknown state schema; manual migration required before writing')
    return s

def log(base,kind,data):
    p=base/'run-log.jsonl';p.parent.mkdir(parents=True,exist_ok=True)
    entry={'at':now(),'event':kind,'details':data}
    with p.open('a',encoding='utf8') as f: f.write(json.dumps(entry,ensure_ascii=False,sort_keys=True)+'\n')

@contextlib.contextmanager
def guard(base):
    base.mkdir(parents=True,exist_ok=True)
    lock=base/'.write.lock'
    try:
        fd=os.open(str(lock),os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    except FileExistsError:
        fail('Another operation holds the lock. Do not delete it while a process may be active.')
    try:
        os.write(fd,f'pid={os.getpid()} at={now()}\n'.encode());os.close(fd)
        yield
    finally:
        lock.unlink(missing_ok=True)

def init(base):
    with guard(base):
        if (base/'state.json').exists():
            s=load_state(base);return {'already_initialized':True,'state_version':s['schema_version']}
        atomic(base/'state.json',{'schema_version':SCHEMA,'created_at':now(),'updated_at':now(),'workflow':'needs_onboarding'})
        atomic(base/'profile.json',{'author_name':None,'audience':None,'goals':[],'platforms':[],'confirmed_facts':[], 'conflicts':[]})
        atomic(base/'voice.json',{'status':'missing','sample_source':'none','rules':{},'confidence':'unverified'})
        atomic(base/'strategy.json',{'status':'not_defined','pillars':[],'assumptions':[]})
        atomic(base/'calendar.json',{'schema_version':SCHEMA,'entries':[]})
        atomic(base/'drafts'/'index.json',{'schema_version':SCHEMA,'by_key':{}})
        log(base,'initialized',{'schema':SCHEMA})
        return {'created':True,'next':'Fill profile with confirmed user facts via set-profile'}

def status(base):
    s=read(base/'state.json')
    if not s: return {'initialized':False,'workflow':'needs_setup','next':'init','drafts_by_status':{},'missing':['profile','voice','strategy']}
    s=load_state(base)
    p=read(base/'profile.json',{})
    v=read(base/'voice.json',{})
    st=read(base/'strategy.json',{})
    idx=read(base/'drafts'/'index.json',{'by_key':{}})
    drafts=[]
    for identifier in idx.get('by_key',{}).values():
        d=read(base/'drafts'/f'{identifier}.json')
        if d: drafts.append(d)
    counts={}
    for d in drafts:counts[d['status']]=counts.get(d['status'],0)+1
    missing=[k for k in ('author_name','audience','goals','platforms') if not p.get(k)]
    if not v or v.get('status')=='missing':missing.append('voice')
    if st.get('status')=='not_defined':missing.append('strategy')
    if counts.get('needs_review',0):nxt='present existing drafts for explicit human approval'
    elif counts.get('draft',0):nxt='resume existing draft; resolve any missing facts needed for its QA'
    elif missing: nxt='complete-onboarding: '+', '.join(missing)
    elif counts.get('approved',0):nxt='offer manual staging after user instructions'
    elif counts.get('manual_handoff',0):nxt='follow up only on user-reported publication'
    else:nxt='ask content objective; research/ideate then draft'
    return {'initialized':True,'workflow':s['workflow'],'missing':missing,'drafts_by_status':counts,'draft_ids':[x['id'] for x in drafts], 'next':nxt,'calendar_entries':len(read(base/'calendar.json',{'entries':[]})['entries'])}

def set_profile(base,filename,replace):
    with guard(base):
        load_state(base)
        new=read(Path(filename)); old=read(base/'profile.json')
        if not isinstance(new,dict):fail('Profile must be a JSON object')
        allowed={'author_name','audience','goals','platforms','confirmed_facts','conflicts','profile_links','topics_to_avoid','brand_type'}
        if any(k not in allowed for k in new):fail('Unknown profile field(s): '+str(set(new)-allowed))
        if 'platforms' in new and (not isinstance(new['platforms'],list) or not set(new['platforms'])<=PLATFORMS):fail('platforms must be list of x, instagram, linkedin')
        if 'goals' in new and not isinstance(new['goals'],list):fail('goals must be array')
        conflict={k:{'saved':old[k],'proposed':v} for k,v in new.items() if old.get(k) not in (None,[],{}) and old.get(k)!=v}
        if conflict and not replace:
            old['conflicts']=old.get('conflicts',[])+[{'at':now(),'proposed':conflict}]
            atomic(base/'profile.json',old);log(base,'profile_conflict',{'keys':list(conflict)})
            fail('Conflicting profile facts preserved for review. Supply --confirm-replacement only after author confirmation.')
        old.update(new);atomic(base/'profile.json',old);log(base,'profile_updated',{'fields':list(new)})
        return {'updated':list(new),'unresolved_conflicts':len(old.get('conflicts',[]))}

def set_voice(base,filename):
    with guard(base):
        load_state(base)
        voice=read(Path(filename))
        if not isinstance(voice,dict) or not isinstance(voice.get('rules'),dict):fail('Voice JSON must include rules object')
        if voice.get('status') not in ('verified','provisional'):fail('Voice status must be verified or provisional')
        if voice['status']=='verified' and (not voice.get('sample_source') or str(voice.get('sample_source')).strip().lower() in ('none','example','template','placeholder')):fail('Verified voice requires real owner writing sample_source')
        atomic(base/'voice.json',voice);log(base,'voice_saved',{'status':voice['status']});return {'status':voice['status']}

def set_strategy(base,filename):
    with guard(base):
        load_state(base)
        val=read(Path(filename))
        if not isinstance(val,dict) or val.get('status') not in ('approved','proposed'):fail('Strategy JSON needs status proposed or approved')
        if not isinstance(val.get('pillars'),list):fail('Strategy requires pillars array')
        atomic(base/'strategy.json',val);log(base,'strategy_saved',{'status':val['status']});return {'status':val['status']}

def draft_path(base,id):
    if not re.fullmatch(r'[a-f0-9]{16}',id):fail('Invalid draft id')
    return base/'drafts'/f'{id}.json'

def draft(base,id):
    d=read(draft_path(base,id))
    if not d:fail(f'Draft {id} not found')
    return d

def save_draft(base,d): d['updated_at']=now();atomic(draft_path(base,d['id']),d)

def set_workflow(base,workflow):
    state=load_state(base);state['workflow']=workflow;state['updated_at']=now();atomic(base/'state.json',state)


def create_draft(base,platform,fmt,title,textfile,key):
    if platform not in PLATFORMS:fail('Unknown platform')
    if fmt not in FORMATS:fail('Unknown format')
    if fmt not in PLATFORM_FORMATS[platform]:fail(f'Unsupported {platform} format: {fmt}. Choose a native format or ask for an adaptation.')
    content=Path(textfile).read_text(encoding='utf8').strip()
    if not content:fail('Cannot create an empty draft')
    if not title.strip():fail('A descriptive title is required')
    rawkey=key.strip() if key else f'{platform}:{fmt}:{title.casefold()}:{hashlib.sha256(content.encode()).hexdigest()[:16]}'
    if len(rawkey)<5:fail('idempotency key must be >=5 characters')
    with guard(base):
        s=load_state(base);idx=read(base/'drafts'/'index.json')
        if rawkey in idx['by_key']:
            ident=idx['by_key'][rawkey]
            existing=draft(base,ident)
            if (existing['platform'], existing['format'], existing['title'], existing['text']) != (platform,fmt,title,content):
                fail('Idempotency key collision: different content or destination under an existing key. Resume/revise existing draft or use a new distinct key.')
            return {'created':False,'duplicate':True,'id':ident,'status':existing['status']}
        ident=hashlib.sha256((rawkey+'\0'+now()).encode()).hexdigest()[:16]
        d={'schema_version':SCHEMA,'id':ident,'key':rawkey,'platform':platform,'format':fmt,'title':title,'text':content,'status':'draft','created_at':now(),'updated_at':now(),'qa':{'verdict':'unreviewed'},'approval':None,'handoff':None,'publication':None}
        save_draft(base,d);idx['by_key'][rawkey]=ident;atomic(base/'drafts'/'index.json',idx)
        s['workflow']='drafting';s['updated_at']=now();atomic(base/'state.json',s)
        log(base,'draft_created',{'id':ident,'platform':platform,'format':fmt});return {'created':True,'id':ident,'status':'draft'}

def qa_draft(base,id,verdict,note):
    if verdict not in ('pass','revise','blocked'):fail('qa verdict must be pass/revise/blocked')
    if not note.strip():fail('QA note is required')
    with guard(base):
        load_state(base);d=draft(base,id)
        if d['status'] not in ('draft','needs_review'):fail('Approved or handed-off copy must first be revised before new QA')
        d['qa']={'verdict':verdict,'note':note,'at':now(),'content_sha256':hashlib.sha256(d['text'].encode()).hexdigest()}
        d['status']='needs_review' if verdict=='pass' else 'draft'
        save_draft(base,d);set_workflow(base,d['status']);log(base,'qa',{'id':id,'verdict':verdict});return {'id':id,'status':d['status'],'qa':verdict}

def approve(base,id,approved_by,note):
    if not approved_by.strip() or not note.strip():fail('Record the human approver name and specific approval note')
    with guard(base):
        load_state(base);d=draft(base,id)
        if d['status']!='needs_review' or d['qa']['verdict']!='pass':fail('Only a QA-passed needs_review draft can be approved')
        if d['qa'].get('content_sha256')!=hashlib.sha256(d['text'].encode()).hexdigest():fail('Draft changed after QA: repeat fact and quality review for exact content before approval')
        d['approval']={'by':approved_by,'note':note,'at':now(),'content_sha256':hashlib.sha256(d['text'].encode()).hexdigest(),'confirmation_type':'user_attested_not_cryptographically_verified'}
        d['status']='approved';save_draft(base,d);set_workflow(base,'approved');log(base,'human_approval_recorded',{'id':id,'by':approved_by})
        return {'id':id,'status':'approved','warning':'User attestation recorded; CLI cannot independently prove who authorized this.'}

def revise(base,id,textfile):
    text=Path(textfile).read_text(encoding='utf8').strip()
    if not text:fail('Cannot replace a draft with empty content')
    with guard(base):
        load_state(base);d=draft(base,id)
        if d['status']=='reported_published':fail('Published historical version is immutable; make a new draft')
        d['text']=text;d['status']='draft';d['qa']={'verdict':'unreviewed'};d['approval']=None;d['handoff']=None
        save_draft(base,d);set_workflow(base,'drafting');log(base,'revised_approval_invalidated',{'id':id});return {'id':id,'status':'draft','approval_invalidated':True}

def stage(base,id):
    with guard(base):
        load_state(base);d=draft(base,id)
        if d['status']!='approved':fail('Explicitly approved draft required for handoff')
        if not d.get('approval') or d['approval'].get('content_sha256')!=hashlib.sha256(d['text'].encode()).hexdigest():
            fail('Content changed after approval. Re-run QA and obtain approval for the exact content.')
        export={'draft_id':id,'platform':d['platform'],'format':d['format'],'text':d['text'],'approval':d['approval'],'status':'manual_handoff','external_scheduler_confirmed':False,'instructions':'Manually paste this into the platform. No publication/scheduling has been performed.'}
        dest=base/'exports'/f'{id}.json';atomic(dest,export)
        d['status']='manual_handoff';d['handoff']={'mode':'manual_export','path':str(dest),'at':now()};save_draft(base,d);set_workflow(base,'manual_handoff')
        log(base,'manual_export_created',{'id':id});return {'id':id,'status':'manual_handoff','path':str(dest),'published':False,'scheduled':False}

def mark_published(base,id,url):
    parsed=urlsplit(url)
    if parsed.scheme!='https' or not parsed.netloc:fail('Provide full https post URL')
    with guard(base):
        load_state(base);d=draft(base,id)
        if d['status']!='manual_handoff':fail('Manual handoff required before recording publication')
        d['status']='reported_published';d['publication']={'url':url,'at':now(),'evidence':'user_reported_not_independently_verified'};save_draft(base,d);set_workflow(base,'reported_published')
        log(base,'reported_published',{'id':id,'url':url});return {'id':id,'status':d['status'],'evidence':d['publication']['evidence']}

def record_metrics(base,id,filename):
    val=read(Path(filename))
    if not isinstance(val,dict) or not val.get('source') or not val.get('observed_at') or not isinstance(val.get('metrics'),dict):fail('Metrics JSON needs source, observed_at and metrics object')
    for k,v in val['metrics'].items():
        if type(v) not in (int,float) or not math.isfinite(v) or v<0:fail('Metrics must be finite nonnegative numbers, never guessed')
    with guard(base):
        load_state(base);d=draft(base,id)
        if d['status']!='reported_published':fail('Record metrics only for user-reported published posts')
        dest=base/'metrics'/f'{id}.json';atomic(dest,{'draft_id':id,**val});log(base,'metrics_recorded',{'id':id,'source':val['source']});return {'id':id,'saved':str(dest),'source':val['source']}

def add_calendar(base,id,planned_at):
    try:
        parsed=datetime.fromisoformat(planned_at)
        if parsed.tzinfo is None:fail('Provide planned_at with an explicit timezone offset')
    except ValueError:fail('planned_at must be offset-aware ISO-8601 time')
    with guard(base):
        load_state(base);d=draft(base,id);cal=read(base/'calendar.json')
        if any(e['draft_id']==id for e in cal['entries']):fail('Calendar already contains this draft; edit existing entry instead')
        entry={'draft_id':id,'platform':d['platform'],'planned_at':planned_at,'status':'planned_only_not_scheduled'}
        cal['entries'].append(entry);atomic(base/'calendar.json',cal);log(base,'calendar_entry_added',{'id':id});return entry

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace',default=str(ROOT/'.social'),help='Directory for private local state. Defaults to repository/.social')
    subs=p.add_subparsers(dest='action',required=True)
    for name in ('init','status','resume'):subs.add_parser(name)
    v=subs.add_parser('set-profile');v.add_argument('file');v.add_argument('--confirm-replacement',action='store_true')
    v=subs.add_parser('set-voice');v.add_argument('file')
    v=subs.add_parser('set-strategy');v.add_argument('file')
    v=subs.add_parser('create-draft');v.add_argument('--platform',required=True);v.add_argument('--format',required=True);v.add_argument('--title',required=True);v.add_argument('--text-file',required=True);v.add_argument('--key',default='')
    for name in ('qa','approve','revise','stage','mark-published','metrics','calendar'):
        v=subs.add_parser(name);v.add_argument('id')
        if name=='qa':v.add_argument('--verdict',required=True);v.add_argument('--note',required=True)
        if name=='approve':v.add_argument('--approved-by',required=True);v.add_argument('--note',required=True)
        if name=='revise':v.add_argument('--text-file',required=True)
        if name=='mark-published':v.add_argument('--url',required=True)
        if name=='metrics':v.add_argument('--file',required=True)
        if name=='calendar':v.add_argument('--at',required=True,help='ISO 8601 including timezone e.g. 2026-11-01T09:00:00+01:00')
    a=p.parse_args(argv);base=Path(a.workspace).resolve()
    try:
        if a.action=='init':out=init(base)
        elif a.action in ('status','resume'):out=status(base)
        elif a.action=='set-profile':out=set_profile(base,a.file,a.confirm_replacement)
        elif a.action=='set-voice':out=set_voice(base,a.file)
        elif a.action=='set-strategy':out=set_strategy(base,a.file)
        elif a.action=='create-draft':out=create_draft(base,a.platform,a.format,a.title,a.text_file,a.key)
        elif a.action=='qa':out=qa_draft(base,a.id,a.verdict,a.note)
        elif a.action=='approve':out=approve(base,a.id,a.approved_by,a.note)
        elif a.action=='revise':out=revise(base,a.id,a.text_file)
        elif a.action=='stage':out=stage(base,a.id)
        elif a.action=='mark-published':out=mark_published(base,a.id,a.url)
        elif a.action=='metrics':out=record_metrics(base,a.id,a.file)
        elif a.action=='calendar':out=add_calendar(base,a.id,a.at)
        else:fail('Unsupported action')
        print(json.dumps(out,indent=2,ensure_ascii=False));return 0
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print(json.dumps({'error':str(e),'action':a.action}),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
