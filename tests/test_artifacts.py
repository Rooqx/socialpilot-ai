import csv,json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class PackagingTests(unittest.TestCase):
    def test_canonical_and_claude_adapter_byte_identical(self):
        src=ROOT/'skills';dst=ROOT/'.claude'/'skills'
        a={p.relative_to(src):p.read_bytes() for p in src.rglob('*') if p.is_file()}
        b={p.relative_to(dst):p.read_bytes() for p in dst.rglob('*') if p.is_file()}
        self.assertEqual(a,b)
    def test_visible_and_agents_adapter_byte_identical(self):
        src=ROOT/'skills';dst=ROOT/'.agents'/'skills'
        a={p.relative_to(src):p.read_bytes() for p in src.rglob('*') if p.is_file()}
        b={p.relative_to(dst):p.read_bytes() for p in dst.rglob('*') if p.is_file()}
        self.assertEqual(a,b)
    def test_visible_skills_are_nonempty(self):
        self.assertEqual(len(list((ROOT/'skills').glob('*/SKILL.md'))),28)
    def test_manifest_28_unique(self):
        m=json.loads((ROOT/'docs'/'manifest.json').read_text())
        self.assertEqual(m['count'],28)
        self.assertEqual(len(set(m['skills'])),28)
        self.assertIn('social-orchestrator',m['skills'])
    def test_every_skill_has_full_contract(self):
        for p in (ROOT/'skills').glob('*/SKILL.md'):
            text=p.read_text()
            self.assertIn('## Required process',text,p)
            self.assertIn('## Recovery',text,p)
            self.assertEqual(re.search(r'^name: (.+)$',text,re.M).group(1),p.parent.name)
    def test_255_source_accounting(self):
        with (ROOT/'docs'/'source-inventory-255.csv').open() as f:
            d=list(csv.DictReader(f))
        self.assertEqual(len(d),255)
        self.assertEqual(len({(x['repository'],x['skill_path']) for x in d}),255)
        self.assertEqual(sum(x['final_audit_decision']=='REJECT_REDIRECT' for x in d),71)
    def test_private_state_gitignored(self):
        g=(ROOT/'.gitignore').read_text();self.assertIn('.social/',g)
    def test_native_skill_entrypoints(self):
        self.assertIn('social-orchestrator', (ROOT/'AGENTS.md').read_text())
        self.assertIn('social-orchestrator', (ROOT/'CLAUDE.md').read_text())
        self.assertIn('social-orchestrator', (ROOT/'GEMINI.md').read_text())
    def test_no_runtime_certification_claim(self):
        self.assertIn('Not tested', (ROOT/'docs'/'RELEASE_STATUS.md').read_text())
        self.assertIn('not cross-agent production certified', (ROOT/'README.md').read_text().lower())
if __name__=='__main__':unittest.main()
