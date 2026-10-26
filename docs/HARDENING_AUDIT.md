# Version 0.2 — hardening and regression audit

**Scope:** This is the first substantive hardening release after the v0.1.1 visibility fix. Changes are local; nothing was pushed to GitHub or social accounts.

## Phase 1 — Identify actual implementation shortcomings

- All 28 short `SKILL.md` entrypoints and their reference directories inspected in the unpacked project.
- Initial entrypoints averaged approximately 330 words: useful for discovery but too thin as a complete specialist operating handbook.
- V0.1.1 contained no offline natural-language routing fixture or deep per-skill playbook, and deterministic QA/approval could be bypassed by directly editing a QA-passed draft JSON before approval.
- Existing idempotency key lookup returned an old draft even if a caller supplied different text with the same key; that would silently discard work.

## Phase 2 — Repair skill depth without bloating startup context

- Added **28 distinct specialist `references/playbook.md` documents**, each with domain-specific procedure, decision criteria, real-world illustrative examples and failure/acceptance checks (approximately 243–546 words each).
- Linked each selected skill to its playbook through a progressive-disclosure section of `SKILL.md`.
- Avoided importing large upstream texts, vendor-specific mandatory dependencies or unverifiable growth multipliers. Kept author identity, metrics and account limits evidence-dependent.
- All 28 canonical skills and 28 playbooks synchronized to the two agent discovery adapter trees; the visible `skills/` tree remains the only editing source.

## Phase 3 — Repair deterministic runtime defects

- Same idempotency key + different content, platform, format or title now produces a **collision error** rather than silently returning old copy.
- QA pass records a SHA-256 of the exact text; approval refuses text changed directly after QA. Existing approval hash continues to protect the export step.
- Platform-format compatibility is validated (e.g. X doesn't silently accept an Instagram Reel format).
- Resume prioritizes an existing draft even when optional onboarding facts are missing.
- Verified voice state rejects `none`, template and placeholder source labels.
- Imported numeric metrics reject NaN and infinity as well as negative values.

## Phase 4 — Test routing and workflow invariants

- Added `scripts/route_preview.py`, a **deterministic, offline diagnostic** that recognizes common intents and proposes minimal skill chains, but cannot invoke an LLM or social provider.
- Added regression tests for 20 routing example phrases, manual approval/export flows across X/LinkedIn/Instagram, collision protection, QA integrity, unsupported format protection, and finite metrics.
- Added `docs/ACCEPTANCE_SCENARIOS.md` with 18 real-agent test cases and a separate human-review rubric.

## Phase 5 — Independent checks and re-audit

Run the commands recorded below on a fresh extraction. Static structural checks and local unit tests can pass; **real-agent behavioral, live data, actual image production and writing-quality evaluations remain open**. No claim of production certification is warranted.

```bash
python3 scripts/lint_skills.py
python3 scripts/sync_adapters.py --check
python3 -m unittest discover -s tests -v
python3 scripts/independent_release_audit.py
python3 scripts/route_preview.py 'Create me a post'
```

## Remaining blocking validations

1. Install/open in a real Claude Code environment; verify discovery and progressive reference loading with observed tool traces.
2. Repeat independently in real Codex, OpenCode and Antigravity runtimes; environment/version-specific behavior is not simulated by Python.
3. Have a human evaluate at least a representative set of generated posts and a genuine user-owned voice sample pack; do not claim model-level writing quality from the existence of playbooks.
4. Verify live platform requirements when creating an actual handoff; static guidance expires.
5. Any future publishing provider needs strong, action-specific authentication, idempotent retries and verified receipts before attempting publication.

**Release verdict:** V0.2 is a stronger *local implementation candidate*, not production-certified.

## Fresh-extraction audit repair

The checksum test initially failed because the existing `independent_release_audit.py` claimed to be read-only but rewrote `docs/independent_release_audit.json` with a new timestamp. Changed its default mode to **read-only**; a report overwrite now requires `--write-report`. This regression was found and fixed by the archive-level audit loop.
