import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from preflight_draft import preflight
class PreflightAudit(unittest.TestCase):
 def test_x_standard_oversize_blocked(self):self.assertEqual('blocked',preflight('a'*281,'x')['status'])
 def test_x_standard_valid(self):self.assertEqual('format_pass_editorial_review_required',preflight('A test sentence.','x')['status'])
 def test_x_extended_requires_entitlement_note(self):self.assertTrue(preflight('a'*300,'x',True)['warnings'])
 def test_linkedin_oversize_blocked(self):self.assertEqual('blocked',preflight('a'*3001,'linkedin')['status'])
 def test_linkedin_3000_valid(self):self.assertNotEqual('blocked',preflight('a'*3000,'linkedin')['status'])
 def test_placeholder_blocks(self):self.assertEqual('blocked',preflight('Welcome [insert data]','instagram')['status'])
 def test_first_person_flags(self):self.assertTrue(any('First-person' in x for x in preflight('I built a service.','x')['warnings']))
 def test_format_pass_is_not_factual_certification(self):self.assertIn('does not verify claims',preflight('Hello','x')['notice'])
 def test_instagram_media_warning(self):self.assertTrue(any('asset' in x for x in preflight('Hello','instagram')['warnings']))
 def test_empty_blocks(self):self.assertEqual('blocked',preflight(' ','x')['status'])
if __name__=='__main__':unittest.main()
