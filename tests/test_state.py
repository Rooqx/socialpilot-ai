"""Functional unit tests for local state manager; not LLM or external-platform tests."""
import importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('socialctl',ROOT/'scripts'/'socialctl.py')
ctl=importlib.util.module_from_spec(spec);spec.loader.exec_module(ctl)

class StateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name)/'.social'
        self.txt=Path(self.tmp.name)/'post.txt'
        self.txt.write_text('A grounded example post.\n')
        self.assertTrue(ctl.init(self.base)['created'])
    def jsonfile(self,filename,data):
        p=Path(self.tmp.name)/filename;p.write_text(json.dumps(data));return str(p)
    def create(self,key='test-x-001'):
        return ctl.create_draft(self.base,'x','post','A useful topic',str(self.txt),key)['id']
    def test_idempotent_initialization(self):
        self.assertTrue(ctl.init(self.base)['already_initialized'])
        self.assertEqual(ctl.status(self.base)['workflow'],'needs_onboarding')
    def test_fresh_onboarding_is_blank(self):
        prof=ctl.read(self.base/'profile.json')
        self.assertIsNone(prof['author_name']);self.assertIsNone(prof['audience']);self.assertFalse(prof['goals'])
    def test_source_aware_profile_no_silent_overwrite(self):
        p=self.jsonfile('profile.json',{'author_name':'Creator A','audience':'devs','platforms':['x','instagram'],'goals':['teach']})
        ctl.set_profile(self.base,p,False)
        q=self.jsonfile('change.json',{'author_name':'Creator B'})
        with self.assertRaisesRegex(ValueError,'Conflicting'):ctl.set_profile(self.base,q,False)
        self.assertEqual(ctl.read(self.base/'profile.json')['author_name'],'Creator A')
        self.assertEqual(len(ctl.read(self.base/'profile.json')['conflicts']),1)
    def test_illegal_platform_rejected(self):
        q=self.jsonfile('bad.json',{'platforms':['myspace']})
        with self.assertRaises(ValueError):ctl.set_profile(self.base,q,False)
    def test_no_voice_samples_cannot_be_verified(self):
        p=self.jsonfile('voice.json',{'status':'verified','rules':{}})
        with self.assertRaises(ValueError):ctl.set_voice(self.base,p)
    def test_duplicate_key_is_safe(self):
        one=ctl.create_draft(self.base,'x','post','One',str(self.txt),'topic-x')
        two=ctl.create_draft(self.base,'x','post','One',str(self.txt),'topic-x')
        self.assertTrue(one['created']);self.assertEqual(one['id'],two['id']);self.assertFalse(two['created'])
    def test_cannot_approve_before_qa(self):
        id=self.create()
        with self.assertRaisesRegex(ValueError,'QA-passed'):ctl.approve(self.base,id,'Creator','Looks good')
    def test_cannot_stage_before_approval(self):
        id=self.create()
        with self.assertRaisesRegex(ValueError,'approved'):ctl.stage(self.base,id)
    def test_blocked_qa_does_not_get_approved(self):
        id=self.create();ctl.qa_draft(self.base,id,'blocked','Unsupported fact')
        with self.assertRaises(ValueError):ctl.approve(self.base,id,'Creator','Approved')
    def test_approval_then_export_never_publishes(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Evidence checked')
        ctl.approve(self.base,id,'Creator','Specific approval for this copy')
        result=ctl.stage(self.base,id)
        self.assertFalse(result['published']);self.assertFalse(result['scheduled'])
        self.assertEqual(ctl.read(Path(result['path']))['status'],'manual_handoff')
    def test_material_revision_invalidates_approval(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Validated');ctl.approve(self.base,id,'Creator','Approved')
        self.txt.write_text('Changed approved content')
        out=ctl.revise(self.base,id,str(self.txt))
        self.assertTrue(out['approval_invalidated']);self.assertIsNone(ctl.draft(self.base,id)['approval'])
        with self.assertRaises(ValueError):ctl.stage(self.base,id)
    def test_reported_publish_requires_full_url(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Validated');ctl.approve(self.base,id,'Creator','Approved');ctl.stage(self.base,id)
        with self.assertRaises(ValueError):ctl.mark_published(self.base,id,'http://example.org/post')
        outcome=ctl.mark_published(self.base,id,'https://example.org/post')
        self.assertEqual(outcome['evidence'],'user_reported_not_independently_verified')
    def test_metrics_reject_fake_or_negative_data(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Validated');ctl.approve(self.base,id,'Creator','Approved');ctl.stage(self.base,id);ctl.mark_published(self.base,id,'https://example.org/post')
        p=self.jsonfile('m1.json',{'source':'export','observed_at':'2026-01-01','metrics':{'likes':-1}})
        with self.assertRaisesRegex(ValueError,'nonnegative'):ctl.record_metrics(self.base,id,p)
        q=self.jsonfile('m2.json',{'source':'manual user export','observed_at':'2026-01-01','metrics':{'likes':2}})
        self.assertTrue(ctl.record_metrics(self.base,id,q)['saved'])
    def test_calendar_has_timezone_and_no_duplicates(self):
        id=self.create()
        with self.assertRaisesRegex(ValueError,'offset-aware'):ctl.add_calendar(self.base,id,'2026-10-27T09:00:00')
        ctl.add_calendar(self.base,id,'2026-10-27T09:00:00+01:00')
        with self.assertRaisesRegex(ValueError,'already contains'):ctl.add_calendar(self.base,id,'2026-10-28T09:00:00+01:00')
        self.assertEqual(ctl.read(self.base/'calendar.json')['entries'][0]['status'],'planned_only_not_scheduled')
    def test_resume_reuses_existing_state_and_ids(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Validated')
        snapshot=ctl.status(self.base)
        self.assertEqual(snapshot['drafts_by_status']['needs_review'],1)
        self.assertIn(id,snapshot['draft_ids']);self.assertIn('approval',snapshot['next'])
    def test_stale_schema_fails_closed(self):
        p=self.base/'state.json';d=ctl.read(p);d['schema_version']=999;ctl.atomic(p,d)
        with self.assertRaisesRegex(ValueError,'Unknown state schema'):ctl.create_draft(self.base,'x','post','A',str(self.txt),'other-id')
    def test_lock_does_not_permit_overlap(self):
        with ctl.guard(self.base):
            with self.assertRaisesRegex(ValueError,'holds the lock'):
                ctl.create_draft(self.base,'x','post','A',str(self.txt),'other-id')
    def test_no_auto_create_status(self):
        self.assertEqual(ctl.status(Path(self.tmp.name)/'nonexistent')['next'],'init')
    def test_approval_hash_prevents_tampered_copy(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Validated');ctl.approve(self.base,id,'Creator','Approved')
        p=self.base/'drafts'/f'{id}.json';d=ctl.read(p);d['text']='Tampered without fresh approval';ctl.atomic(p,d)
        with self.assertRaisesRegex(ValueError,'Content changed after approval'):ctl.stage(self.base,id)
    def test_workflow_tracks_review_approval_and_handoff(self):
        id=self.create();self.assertEqual(ctl.status(self.base)['workflow'],'drafting')
        ctl.qa_draft(self.base,id,'pass','Validated')
        self.assertEqual(ctl.status(self.base)['workflow'],'needs_review')
        ctl.approve(self.base,id,'Creator','Approved')
        self.assertEqual(ctl.status(self.base)['workflow'],'approved')
        ctl.stage(self.base,id)
        self.assertEqual(ctl.status(self.base)['workflow'],'manual_handoff')
    def test_published_post_is_immutable(self):
        id=self.create();ctl.qa_draft(self.base,id,'pass','Validated');ctl.approve(self.base,id,'Creator','Approved');ctl.stage(self.base,id);ctl.mark_published(self.base,id,'https://example.org/post')
        with self.assertRaises(ValueError):ctl.revise(self.base,id,str(self.txt))

if __name__=='__main__':unittest.main()
