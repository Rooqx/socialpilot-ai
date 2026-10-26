"""Fixture tests for offline routing specification, not LLM performance."""
import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('route_preview', ROOT/'scripts'/'route_preview.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class RouteTests(unittest.TestCase):
    def test_basic_intent_matrix(self):
        pairs={
            'I need posts':'draft',
            'create me a post':'draft',
            'Write five X posts':'draft',
            'Write a LinkedIn post':'draft',
            'Can you do an Instagram caption?':'draft',
            'I want to start posting':'start',
            'I need posts for this week':'calendar',
            'What should I post next week?':'calendar',
            'Continue where we stopped':'resume',
            'Build an X thread':'thread',
            'Make an Instagram carousel':'carousel',
            'Write a Reel script':'reel',
            'Turn this into 3 platform posts':'repurpose',
            'Repurpose this article':'repurpose',
            'Analyze my post metrics':'analytics',
            'Find conversations about developer tooling':'listen',
            'Optimize my LinkedIn bio':'profile',
            'Post this':'handoff',
            'Schedule the approved copy':'handoff',
            'Can you help?':'unknown',
        }
        for prompt,intent in pairs.items():
            with self.subTest(prompt=prompt):
                output=mod.plan(prompt)
                self.assertEqual(output['intent'],intent)
                self.assertFalse(output['external_actions_allowed'])
    def test_platform_routes_are_distinct(self):
        self.assertIn('x-post-writer',mod.plan('Write five X posts')['skills'])
        self.assertIn('linkedin-post-writer',mod.plan('Create a LinkedIn post')['skills'])
        self.assertIn('instagram-caption-writer',mod.plan('Write Instagram caption')['skills'])
    def test_missing_platform_asks_one_question(self):
        a=mod.plan('Create me a post')
        self.assertEqual(len(a['blocking_questions']),1)
        b=mod.plan('Create me a post', saved_default='x')
        self.assertFalse(b['blocking_questions'])
    def test_existing_draft_takes_priority(self):
        a=mod.plan('I need posts',existing_draft=True)
        self.assertEqual(a['intent'],'resume_existing_draft')
        self.assertNotIn('x-post-writer',a['skills'])
    def test_publishing_never_auto_authorizes(self):
        for s in ('Post this','Schedule the approved copy','publish to LinkedIn'):
            self.assertFalse(mod.plan(s)['external_actions_allowed'])
if __name__=='__main__':unittest.main()
