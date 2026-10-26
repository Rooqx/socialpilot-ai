# Portable Social Media Agent

**Status: v0.3 source-fidelity hardened local candidate — not cross-agent production certified.**

An agent-skills system for X, Instagram and LinkedIn. Based on a 255-source-skill audit, the repository contains 28 original consolidated `SKILL.md` workflows, a natural-language orchestrator, human-approval gates, a local persistent-state CLI and version-pinned source provenance.

## Start in any agent

1. Open the entire repository folder in Claude Code, Codex, OpenCode or Antigravity.
2. Make sure the agent reads `AGENTS.md` (Claude additionally has `CLAUDE.md`; Antigravity has `GEMINI.md`). Skill discovery must be verified on each runtime.
3. Say **“I want to start posting.”** The agent first recovers `.social` state; on a fresh installation it initializes blank profile/voice/strategy and asks for missing essentials before drafting.
4. It can research, propose calendar entries, write per-platform drafts, do QA, and prepare handoffs. **It cannot autonomously publish**, and it never assumes a connected social-media API.

Requires Python 3.10+ for state manager and tests. Skill Markdown can be read without Python, but automated state persistence then requires a manual fallback.

## Where are the skills?

**Open `skills/` at the project root.** Every skill has its own concise `SKILL.md`, a substantive specialist `references/playbook.md`, provenance mapping, and per-skill checks. This directory is visible even when your file browser hides dot-prefixed directories. Agent discovery paths `.agents/skills` and `.claude/skills` are intentionally hidden by the file manager on some devices; they are auto-synced copies.

**Edit only `skills/`**, then run `python3 scripts/sync_adapters.py` to propagate changes. Do not copy individual skills by hand into an adapter or make one adapter your source of truth.

## Inspect without an agent

```bash
python3 scripts/socialctl.py status
python3 scripts/socialctl.py init
python3 scripts/socialctl.py status
python3 scripts/lint_skills.py
python3 scripts/route_preview.py "Create me a post"  # offline diagnostic only
python3 scripts/sync_adapters.py --check
python3 -m unittest discover -s tests -v
```

For a CLI draft smoke test (not publication):

```bash
printf 'An illustrative draft for manual review.\n' > /tmp/post.txt
python3 scripts/socialctl.py create-draft --platform x --format post --title 'Sample' --key 'demo-x-001' --text-file /tmp/post.txt
# Use the draft id from output for qa; approval is a separate human action.
```

## Repository

- `skills/*/SKILL.md`: **visible, canonical collection of 28 editable skills**, with checks and source maps. Start here when browsing or editing.
- `.agents/skills/`: generated copies for Codex/OpenCode/Antigravity; do not edit these directly.
- `.claude/skills/`: generated copies for Claude Code; do not edit these directly.
- `python3 scripts/sync_adapters.py`: updates both hidden agent folders after editing `skills/`. Use `--check` to confirm they match.
- `scripts/socialctl.py`: local-only state manager; no social API calls.
- `scripts/route_preview.py`: offline deterministic intent-routing preview; **not an AI model test**.
- `docs/HARDENING_AUDIT.md`: specific v0.2 changes, repair log and remaining blockers.
- `docs/ACCEPTANCE_SCENARIOS.md`: 18 adversarial real-agent evaluation cases and human scoring protocol.
- `docs/workflow-router.md`: intent routing, skill graph and fallback paths.
- `docs/state-contract.md`: durable file and workflow schemas.
- `docs/platform-playbooks.md`: per-platform format decisions; volatile limits need live verification.
- `docs/quality-gates.md`: hard QA/recovery/approval gates.
- `docs/source-inventory-255.csv`: complete original-source disposition register.
- `docs/skill-selection.csv`: consolidated comparison and provenance.
- `.social/`: private personal data and operational state; generated locally and **gitignored**.

## Privacy and publication

This package never asks for passwords or tokens in chat, never stores API keys in versioned profile files and has no automatic social posting. Manual exports are marked `manual_handoff`; reported links are marked `reported_published`, not platform-verified. Approval flags are user-attested and not cryptographic proof of human identity.

## V0.2 improvement highlights

All 28 skills now have progressive-loading, skill-specific playbooks. Local tests cover draft-key collisions, content-bound QA and approval, unsupported platform/format combinations, multi-platform handoff, missing author sample evidence and invalid numeric metrics. Routing preview exercises common prompt patterns without implying that a live language model was invoked. See `docs/HARDENING_AUDIT.md`.

## Known release blockers

No real agent runtime cold-start tests have been performed here, no live social publishing integration was installed/tested, and subjective content quality needs human evaluation with real (consented) voice examples. Structural and CLI tests cannot establish post reach or model-level performance. See `docs/RELEASE_STATUS.md`.

## Attribution

The curated instructions are a deeper source-faithful, independently authored synthesis (150 methods plus original playbooks), not wholesale copies. `docs/THIRD_PARTY_SOURCES.md` and each skill's `references/source-map.md` identify research sources and pinned versions. Before redistributing third-party code or assets, examine their actual licenses separately; no such code or logos are included here.

## v0.3 source-faithful release additions

**Start at the visible `skills/` folder.** Each of 28 skills now contains a long-form `references/field-manual.md` and a per-method `references/source-fidelity.md` with original upstream provenance. The source inventory retains all 255 original skills, `docs/source-lock.json` identifies 103 commit-pinned original skills and reference guides, and `docs/SOURCE_COVERAGE_REVIEW.md` tracks what was included or deliberately excluded. No upstream executable software or complete copyrighted source file is vendored into the ZIP.

The orchestrator uses `docs/ORCHESTRATOR_EXECUTION_CONTRACT.md` and progressive loading: recover state first, select minimal specialist chain, read deep playbooks only when selected, record evidence, run QA and request human authorization before any external action. `scripts/preflight_draft.py` checks conservative format issues but **is not a factual verifier or a publisher**. `docs/PLATFORM_EVIDENCE_REGISTER.md` records official current sources for X, LinkedIn and Instagram and rejects unverified numerical algorithm hacks.

**Repeatable local validation:**

```bash
python3 scripts/verify_upstream.py --check-manifest
python3 scripts/lint_skills.py
python3 scripts/sync_adapters.py --check
python3 -m unittest discover -s tests -v
python3 scripts/independent_release_audit.py
```

**Unexecuted real-agent trials:** `evals/scenarios.json` contains 44 skill and adversarial prompts. Follow `docs/REAL_AGENT_TRIAL_PROTOCOL.md` in Claude Code, Codex, OpenCode and Antigravity. Those tests and actual writing-quality outcomes are *not* passed here; do not represent them as completed.

**Growth expectation:** We build useful, source-backed, audience-native content and use measured feedback to improve. No algorithm research or automated checklist can guarantee likes, reach, views or follower growth.
