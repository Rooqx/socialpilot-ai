#!/usr/bin/env python3
"""Deterministic lint of compiled skill files and provenance; no LLM score implied."""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CAP=ROOT/'skills';MANIFEST=json.loads((ROOT/'docs'/'manifest.json').read_text())
problems=[]

def check(cond,msg):
    if not cond:problems.append(msg)
paths=sorted(CAP.glob('*/SKILL.md'))
check(len(paths)==28,f'Expected 28 canonical skill files, found {len(paths)}')
check(set(x.parent.name for x in paths)==set(MANIFEST['skills']),'Skill manifest drift')
selection=list(csv.DictReader((ROOT/'docs'/'skill-selection.csv').open()))
source=list(csv.DictReader((ROOT/'docs'/'source-inventory-255.csv').open()))
check(len(selection)==28,'Expected 28 capability mappings')
check(len(source)==255,'Expected 255 source dispositions')
check(len({(x['repository'],x['skill_path']) for x in source})==255,'Duplicate source row detected')
check(set(x['target_skill'] for x in selection)==set(MANIFEST['skills']),'Selection matrix skill mismatch')
check(not any(x['final_audit_decision']=='REJECT_REDIRECT' and x['selected_skill'] for x in source),'Deprecated alias accidentally selected')
for p in paths:
    text=p.read_text(encoding='utf8')
    fm=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
    check(fm is not None,f'{p}: missing frontmatter')
    if fm:
        name=re.search(r'^name:\s*(\S+)',fm.group(1),re.M)
        desc=re.search(r'^description:\s*".+"$',fm.group(1),re.M)
        check(bool(name) and name.group(1)==p.parent.name,f'{p}: name/directory mismatch')
        check(bool(desc),f'{p}: empty/non-string description')
        if desc:
            try:json.loads(desc.group(0).split(': ',1)[1])
            except ValueError:problems.append(f'{p}: invalid quoted description')
    for h in ('## Required process','## Deliverable contract','## Non-negotiable boundaries','## Acceptance tests','## Recovery'):
        check(h in text,f'{p}: missing {h}')
    check(text.count('\n1. ')==1,f'{p}: workflow missing first step')
    check(text.count('\n2. ')>=1,f'{p}: workflow too short')
    check(len(text)>=1500,f'{p}: low detail')
    check((p.parent/'references'/'source-map.md').exists(),f'{p}: missing source map')
    check((p.parent/'references'/'checks.md').exists(),f'{p}: missing skill tests')
    check('without explicit user authorization' in text or 'approval' in text.lower(),f'{p}: no approval boundary')
    check('../../../docs/quality-gates.md' in text, f'{p}: missing shared quality reference')
    check((ROOT/'docs'/'quality-gates.md').exists(),'Missing shared QA file')
    check(p.parent.name not in ('twitter-x-posts','linkedin-posts'),'Accidental upstream directory name')
    check(not re.search(r'(?i)guaranteed (?:viral|reach)|(?:will|must) (?:always )?(?:multiply|boost) reach by \d',text),f'{p}: unsafe deterministic virality claim')
    check(not re.search(r'(?i)\b(?:sk-ant-[\w-]+|ghp_[A-Za-z0-9]{20,})\b',text),f'{p}: possible credential')

# Compare both generated discovery directories with visible canonical skills/.
canonical={p.relative_to(CAP):p.read_bytes() for p in CAP.rglob('*') if p.is_file()}
for adapter_name in ('.agents/skills', '.claude/skills'):
    clone=ROOT/adapter_name
    adapters={p.relative_to(clone):p.read_bytes() for p in clone.rglob('*') if p.is_file()}
    check(canonical==adapters,f'{adapter_name} differs from visible canonical skill tree')
for needed in ('AGENTS.md','CLAUDE.md','GEMINI.md','README.md','docs/workflow-router.md','docs/platform-playbooks.md','docs/state-contract.md','docs/RELEASE_STATUS.md','docs/THIRD_PARTY_SOURCES.md','scripts/socialctl.py','scripts/sync_adapters.py'):
    check((ROOT/needed).exists(),f'Missing required package file: {needed}')
print(f'Compiled skill lint: {len(paths)} canonical skills; {len(canonical)} canonical files; {len(source)} source records; {len(problems)} errors')
for x in problems:print('ERROR:',x)
sys.exit(1 if problems else 0)
