"""Independent static source fidelity and adversarial readiness checks."""
import unittest, json, re, csv, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class FidelityAudit(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.skills=sorted((ROOT/'skills').glob('*/SKILL.md'))
  cls.ledger=json.loads((ROOT/'docs/source-method-ledger.json').read_text())['methods']
  cls.sources=json.loads((ROOT/'docs/source-lock.json').read_text())['sources']
  cls.evals=json.loads((ROOT/'evals/scenarios.json').read_text())['scenarios']
 def test_28_compiled_skills(self):self.assertEqual(28,len(self.skills))
 def test_150_distinct_methods(self):
  self.assertEqual(150,len(self.ledger));self.assertEqual(150,len(set(x['method_id'] for x in self.ledger)))
 def test_all_skills_have_specific_methods(self):
  for file in self.skills:
   slug=file.parent.name
   self.assertGreaterEqual(sum(x['skill']==slug for x in self.ledger),5,slug)
 def test_advanced_reference_really_has_content(self):
  for file in self.skills:
   p=file.parent/'references/field-manual.md';s=p.read_text()
   self.assertGreater(len(s.split()),520,str(p))
   self.assertIn('## Expert techniques and choices',s)
   self.assertIn('## Demonstration',s)
 def test_source_fidelity_references_present(self):
  for file in self.skills:
   self.assertIn('references/source-fidelity.md',file.read_text())
   self.assertTrue((file.parent/'references/source-fidelity.md').exists())
 def test_sources_pin_commit_not_head(self):
  self.assertGreaterEqual(len(self.sources),100)
  for s in self.sources:
   self.assertRegex(s['commit'],r'^[a-f0-9]{40}$')
   self.assertEqual(s['url'],f'https://github.com/{s["repository"]}/blob/{s["commit"]}/{s["path"]}')
 def test_pinned_sources_are_unique(self):
  self.assertEqual(len(self.sources),len({(s['repository'],s['commit'],s['path']) for s in self.sources}))
 def test_no_unlicensed_upstream_copied_into_package(self):
  self.assertFalse((ROOT/'.source-cache').exists())
  self.assertFalse((ROOT/'vendor').exists())
 def test_every_method_implementation_file_exists(self):
  for entry in self.ledger:self.assertTrue((ROOT/entry['implementation_file']).exists())
 def test_evals_include_each_skill(self):
  ids={x['skill'] for x in self.evals}
  self.assertEqual({x.parent.name for x in self.skills},ids)
 def test_adversarial_coverage(self):
  self.assertGreaterEqual(sum(x['type']=='adversarial' for x in self.evals),15)
 def test_no_model_tests_falsely_marked_executed(self):
  self.assertTrue(all(x['executed'] is False for x in self.evals))
 def test_source_status_disclosed(self):
  self.assertTrue(all('NOT_BUNDLED' in x['source_status'] or 'NOT_A_USER' in x['source_status'] for x in self.sources))
 def test_platform_primary_evidence(self):
  s=(ROOT/'docs/PLATFORM_EVIDENCE_REGISTER.md').read_text()
  for name in ('xai-org/x-algorithm','help.x.com','news.linkedin.com','ai.meta.com'):
   self.assertIn(name,s)
  self.assertIn('Do **not** carry',s)
 def test_orchestrator_recovery_and_human_gate(self):
  s=(ROOT/'docs/ORCHESTRATOR_EXECUTION_CONTRACT.md').read_text()
  for term in ('status','idempot','approval','manual_handoff','reported_published','No internet','resume'):
   self.assertIn(term,s)
 def test_no_claim_that_runtime_evals_passed(self):
  self.assertIn('NOT yet completed',(ROOT/'docs/REAL_AGENT_TRIAL_PROTOCOL.md').read_text())
 def test_source_disposition_255_no_missing(self):
  with (ROOT/'docs/source-inventory-255.csv').open() as f:rs=list(csv.DictReader(f))
  self.assertEqual(255,len(rs))
  self.assertEqual(255,len({(x['repository'],x['skill_path']) for x in rs}))
 def test_live_account_changes_not_implemented(self):
  s=(ROOT/'scripts/socialctl.py').read_text()
  self.assertNotIn('requests.post(',s)
  self.assertNotIn('urllib.request.urlopen(',s)
  self.assertIn('manual_handoff',s)
 def test_gitignore_private_data(self):
  s=(ROOT/'.gitignore').read_text()
  self.assertIn('.social/',s);self.assertIn('.source-cache/',s)
 def test_all_adapters_synchronized(self):
  for file in self.skills:
   for adapter in ('.agents/skills','.claude/skills'):
    cp=ROOT/adapter/file.parent.name/'SKILL.md'
    self.assertEqual(hashlib.sha256(cp.read_bytes()).digest(),hashlib.sha256(file.read_bytes()).digest())
if __name__=='__main__':unittest.main()
