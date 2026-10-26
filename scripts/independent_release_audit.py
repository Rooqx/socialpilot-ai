#!/usr/bin/env python3
"""Independent read-only packaging audit. Static only, not model/runtime certification."""
import csv, hashlib, json, re, subprocess, sys, argparse
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parent.parent
CAP=ROOT/'skills';CL=ROOT/'.claude'/'skills';AG=ROOT/'.agents'/'skills'
source=list(csv.DictReader((ROOT/'docs'/'source-inventory-255.csv').open()))
sel=list(csv.DictReader((ROOT/'docs'/'skill-selection.csv').open()))
canon=sorted(CAP.glob('*/SKILL.md'))
checks={}
def test(n,flag):checks[n]=bool(flag)
test('28_skills_exact',len(canon)==28 and len({p.parent.name for p in canon})==28)
test('255_source_unique',len(source)==255 and len({(s['repository'],s['skill_path']) for s in source})==255)
test('71_redirects_excluded',sum(s['final_audit_decision']=='REJECT_REDIRECT' for s in source)==71 and all(not s['selected_skill'] for s in source if s['final_audit_decision']=='REJECT_REDIRECT'))
test('all_target_mapped',len(sel)==28 and {x['target_skill'] for x in sel}=={p.parent.name for p in canon})
test('positive_skill_descriptions',all(re.search(r'^description: ".{30,}"$',p.read_text(),re.M) for p in canon))
test('name_directory_match',all(re.search(r'^name: ([\w-]+)',p.read_text(),re.M).group(1)==p.parent.name for p in canon))
test('distinct_workflow',len({re.search(r'## Required process\n\n(.{0,180})',p.read_text(),re.S).group(1) for p in canon})==28)
test('all_have_source_maps',all((p.parent/'references/source-map.md').exists() for p in canon))
test('all_have_per_skill_acceptance',all((p.parent/'references/checks.md').exists() for p in canon))
test('references_have_source_urls',all('https://github.com/' in (p.parent/'references/source-map.md').read_text() for p in canon))
test('claude_adapters_complete',all((CL/p.parent.name/'SKILL.md').exists() and (CL/p.parent.name/'SKILL.md').read_bytes()==p.read_bytes() for p in canon))
test('agents_adapters_complete',all((AG/p.parent.name/'SKILL.md').exists() and (AG/p.parent.name/'SKILL.md').read_bytes()==p.read_bytes() for p in canon))
test('agent_entrypoints',all((ROOT/f).exists() for f in ('AGENTS.md','CLAUDE.md','GEMINI.md')))
test('state_gitignored','.social/' in (ROOT/'.gitignore').read_text())
test('strict_no_autopublish','no automatic social posting' in (ROOT/'README.md').read_text() and 'No network publishing' in (ROOT/'docs/quality-gates.md').read_text())
test('approval_copy_hash_checked','content_sha256' in (ROOT/'scripts/socialctl.py').read_text() and 'Content changed after approval' in (ROOT/'scripts/socialctl.py').read_text())
test('runtime_certification_explicitly_blocked',all(f'| Cold start in {n} | Not tested |' in (ROOT/'docs/RELEASE_STATUS.md').read_text() for n in ('Claude Code','Codex','OpenCode','Antigravity')))
# v0.3 expanded source-fidelity, security and truthful-certification gates.
ledger=json.loads((ROOT/'docs'/'source-method-ledger.json').read_text())['methods']
locked=json.loads((ROOT/'docs'/'source-lock.json').read_text())['sources']
evals=json.loads((ROOT/'evals'/'scenarios.json').read_text())['scenarios']
test('150_source_derived_methods',len(ledger)==150 and len(set(x['method_id'] for x in ledger))==150)
test('all_28_have_advanced_manuals',all((p.parent/'references/field-manual.md').exists() and len((p.parent/'references/field-manual.md').read_text().split())>520 for p in canon))
test('all_28_have_method_level_source_fidelity',all((p.parent/'references/source-fidelity.md').exists() for p in canon))
test('at_least_100_commit_pinned_upstreams',len(locked)>=100 and all(re.fullmatch(r'[a-f0-9]{40}',x['commit']) for x in locked))
test('pinned_sources_unique',len(locked)==len({(x['repository'],x['commit'],x['path']) for x in locked}))
test('44_unexecuted_model_eval_scenarios',len(evals)==44 and all(x['executed'] is False for x in evals))
test('algorithm_evidence_primary_sources',all(x in (ROOT/'docs'/'PLATFORM_EVIDENCE_REGISTER.md').read_text() for x in ('xai-org/x-algorithm','help.x.com','news.linkedin.com','ai.meta.com')))
test('orch_contract_and_manual_gate',(ROOT/'docs'/'ORCHESTRATOR_EXECUTION_CONTRACT.md').exists() and 'manual_handoff' in (ROOT/'docs'/'ORCHESTRATOR_EXECUTION_CONTRACT.md').read_text())
test('no_source_cache_committed',not (ROOT/'.source-cache').exists() and '.source-cache/' in (ROOT/'.gitignore').read_text())
test('source_coverage_review_exists',(ROOT/'docs/SOURCE_COVERAGE_REVIEW.md').exists() and '71' in (ROOT/'docs/SOURCE_COVERAGE_REVIEW.md').read_text())
prohibited=['ghp_'+'a'*25,'sk-ant-'+'a'*20]
alltexts='\n'.join(p.read_text() for p in ROOT.rglob('*.md') if '/docs/source-inventory' not in str(p))
test('no_sample_private_creds',not any(t in alltexts for t in prohibited))
test('nonempty_docs',all((ROOT/'docs'/n).stat().st_size>1000 for n in ('state-contract.md','quality-gates.md','workflow-router.md','THIRD_PARTY_SOURCES.md')))
# Explicit hard blockers are not false failures of static phase: gate must stay OPEN.
release={'timestamp_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'audit':'independent_read_only_static','checks':checks,'passed':sum(checks.values()),'total':len(checks),'static_pass':all(checks.values()),'production_ready':False,'uncertified':['Claude Code cold start','Codex cold start','OpenCode cold start','Antigravity cold start','LLM output quality evaluation','live social provider integrations','user-specific voice calibration','user-approved GitHub destination']}
# Do not mutate tracked files during an independent read-only audit.
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--write-report',action='store_true',help='Explicitly overwrite tracked audit JSON; not used during packaging smoke checks')
args=parser.parse_args()
if args.write_report:
    (ROOT/'docs'/'independent_release_audit.json').write_text(json.dumps(release,indent=2)+'\n')
print(json.dumps({'passed':release['passed'],'total':release['total'],'static_pass':release['static_pass'],'production_ready':False,'failed':[k for k,v in checks.items() if not v]},indent=2))
sys.exit(0 if all(checks.values()) else 1)
