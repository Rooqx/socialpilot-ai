"""Independent v0.2 regression and local-workflow tests.
These exercise deterministic artifacts and the local state manager, NOT any remote LLM or social API.
"""
import hashlib
import importlib.util
import json
import math
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('hardening_socialctl', ROOT/'scripts'/'socialctl.py')
ctl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctl)

class HardeningContracts(unittest.TestCase):
    def test_every_specialist_has_unique_substantive_playbook(self):
        skills = sorted((ROOT/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills), 28)
        for skill in skills:
            ref = skill.parent/'references'/'playbook.md'
            with self.subTest(skill=skill.parent.name):
                self.assertTrue(ref.is_file())
                body = ref.read_text(encoding='utf8')
                self.assertGreaterEqual(len(body.split()), 220)
                self.assertIn('references/playbook.md', skill.read_text())
                self.assertTrue(any(x in body.lower() for x in ('example','scenario','case','illustration')))
                self.assertTrue(any(x in body.lower() for x in ('failure','check','test','risk','gate')))
    def test_playbooks_are_not_identical_padding(self):
        content = [p.read_bytes() for p in (ROOT/'skills').glob('*/references/playbook.md')]
        self.assertEqual(len(content), len(set(hashlib.sha256(x).hexdigest() for x in content)))
    def test_platforms_have_distinct_native_writing_constraints(self):
        for n in ('x-post-writer','x-thread-writer','linkedin-post-writer','instagram-caption-writer'):
            with self.subTest(n=n):
                s=(ROOT/'skills'/n/'references'/'playbook.md').read_text()
                self.assertGreater(len(s.split()),225)
        s=(ROOT/'skills'/'instagram-caption-writer'/'references'/'playbook.md').read_text()
        self.assertIn('brief_only',s)
        self.assertIn('rendered_verified',s)
    def test_orchestrator_has_smallest_chain_and_durable_recovery(self):
        s=(ROOT/'skills'/'social-orchestrator'/'references'/'playbook.md').read_text()
        for term in ('I need a post','I need posts this week','Continue','post','duplicate','approval'):
            self.assertIn(term.lower(),s.lower())
    def test_hard_gates_not_mistaken_for_editorial_scores(self):
        s=(ROOT/'skills'/'post-qa'/'references'/'playbook.md').read_text()
        self.assertIn('hard gate',s.lower())
        self.assertIn('not a prediction',s.lower())
    def test_no_claim_of_real_agent_production_certification(self):
        s=(ROOT/'docs'/'RELEASE_STATUS.md').read_text().lower()
        self.assertIn('not tested',s)

class HardeningWorkflow(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name)
        self.base=self.folder/'.social'
        ctl.init(self.base)
        self.p=self.folder/'copy.txt'
        self.p.write_text('Retries can repeat work if operations are not idempotent.\n')
    def make(self,platform='x',fmt='post',key='retries-demo',title='Retry example'):
        return ctl.create_draft(self.base,platform,fmt,title,str(self.p),key)['id']
    def test_reuse_identical_draft_is_idempotent(self):
        ident=self.make()
        a=ctl.create_draft(self.base,'x','post','Retry example',str(self.p),'retries-demo')
        self.assertFalse(a['created'])
        self.assertEqual(a['id'],ident)
    def test_same_key_different_content_cannot_silently_reuse(self):
        ident=self.make()
        self.p.write_text('A different claim, different copy')
        with self.assertRaisesRegex(ValueError,'Idempotency key collision'):
            self.make()
        self.assertEqual(ctl.draft(self.base,ident)['text'],'Retries can repeat work if operations are not idempotent.')
    def test_same_key_different_platform_cannot_silently_reuse(self):
        self.make()
        with self.assertRaisesRegex(ValueError,'Idempotency key collision'):
            self.make('linkedin','post')
    def test_invalid_format_for_destination_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'Unsupported x format'):
            self.make('x','reel')
        with self.assertRaisesRegex(ValueError,'Unsupported instagram format'):
            self.make('instagram','thread')
        self.assertEqual(ctl.status(self.base)['drafts_by_status'],{})
    def test_valid_platform_formats(self):
        for name,fmt in [('x','thread'),('linkedin','document'),('instagram','carousel')]:
            with self.subTest(name=name):
                ident=self.make(name,fmt,f'{name}-format-demo',f'{name}-topic')
                self.assertEqual(ctl.draft(self.base,ident)['format'],fmt)
    def test_qa_hash_prevents_approval_of_edited_copy(self):
        ident=self.make()
        ctl.qa_draft(self.base,ident,'pass','Human-reviewed draft in controlled example')
        d=ctl.draft(self.base,ident)
        d['text']='Altered after QA without a new QA pass'
        ctl.atomic(ctl.draft_path(self.base,ident),d)
        with self.assertRaisesRegex(ValueError,'changed after QA'):
            ctl.approve(self.base,ident,'Creator','Approved as originally reviewed')
        self.assertIsNone(ctl.draft(self.base,ident)['approval'])
    def test_verified_voice_needs_real_source_not_none_label(self):
        for source in ('none','placeholder','template'):
            with self.subTest(source=source):
                f=self.folder/f'voice-{source}.json'
                f.write_text(json.dumps({'status':'verified','rules':{'short_openings':True},'sample_source':source}))
                with self.assertRaisesRegex(ValueError,'real owner writing'):
                    ctl.set_voice(self.base,str(f))
    def test_metric_nan_infinity_rejected(self):
        ident=self.make()
        ctl.qa_draft(self.base,ident,'pass','Grounding manually reviewed')
        ctl.approve(self.base,ident,'Creator','Approve exact text for export')
        ctl.stage(self.base,ident)
        ctl.mark_published(self.base,ident,'https://example.org/post')
        for bad in (float('nan'),float('inf'),float('-inf')):
            with self.subTest(bad=bad):
                p=self.folder/'invalid-metrics.json'
                p.write_text(json.dumps({'source':'user-provided export','observed_at':'2026-10-01','metrics':{'views':bad}}))
                with self.assertRaisesRegex(ValueError,'finite nonnegative'):
                    ctl.record_metrics(self.base,ident,str(p))
    def test_draft_resumes_even_with_incomplete_profile(self):
        ident=self.make()
        snap=ctl.status(self.base)
        self.assertIn('resume existing draft',snap['next'])
        self.assertIn(ident,snap['draft_ids'])
    def test_three_platform_handoffs_remain_manual(self):
        identities=[]
        for platform,fmt in [('x','post'),('linkedin','post'),('instagram','carousel')]:
            ident=self.make(platform,fmt,f'flow-{platform}',f'{platform} retry note')
            identities.append(ident)
            ctl.qa_draft(self.base,ident,'pass','Simulated QA for local-state test only; not editorial certification')
            ctl.approve(self.base,ident,'Simulated user','Local test attestation for this exact version')
            out=ctl.stage(self.base,ident)
            self.assertFalse(out['scheduled'])
            self.assertFalse(out['published'])
            self.assertEqual(ctl.read(Path(out['path']))['status'],'manual_handoff')
        snap=ctl.status(self.base)
        self.assertEqual(snap['drafts_by_status']['manual_handoff'],3)
        self.assertEqual(len(set(identities)),3)
    def test_external_post_never_happens_from_staging(self):
        ident=self.make()
        ctl.qa_draft(self.base,ident,'pass','Simulated local review')
        ctl.approve(self.base,ident,'Simulated user','Attestation for export')
        out=ctl.stage(self.base,ident)
        data=ctl.read(Path(out['path']))
        self.assertIn('Manually paste',data['instructions'])
        self.assertIsNone(ctl.draft(self.base,ident)['publication'])
    def test_revise_after_staging_returns_to_unreviewed(self):
        ident=self.make()
        ctl.qa_draft(self.base,ident,'pass','Simulated local review')
        ctl.approve(self.base,ident,'Simulated user','Attestation for export')
        ctl.stage(self.base,ident)
        self.p.write_text('Improved text needs an additional review')
        ctl.revise(self.base,ident,str(self.p))
        d=ctl.draft(self.base,ident)
        self.assertIsNone(d['approval'])
        self.assertEqual(d['qa']['verdict'],'unreviewed')
        with self.assertRaises(ValueError):ctl.stage(self.base,ident)

if __name__=='__main__':unittest.main()
