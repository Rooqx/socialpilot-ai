# Claude Code project entry

Read `AGENTS.md` at this repository root first and follow it. On generic messages like “I want to start posting”, use `.claude/skills/social-orchestrator/SKILL.md`, run `python3 scripts/socialctl.py status`, recover state and select the minimum needed specialized skills. `.claude/skills/` are generated copies of the visible canonical `skills/`, not independent editable versions; `python3 scripts/sync_adapters.py --check` detects drift.

Never send, publish, change accounts, or schedule externally without explicit user authorization. Missing tools mean brief/draft-only results, not fabricated success. Preserve `.social/` private local state and pending approval status. See `docs/quality-gates.md`.

**Specialist loading (v0.3):** After selecting a skill, read its `references/playbook.md` and `references/field-manual.md` for detailed domain decisions, methods, and worked examples. Read `references/source-fidelity.md` when auditing provenance. Load playbooks **only for selected skills**; do not eagerly load all 28. Use `scripts/route_preview.py` only as a dry-run route diagnostic, never as evidence that an AI agent has actually chosen or executed a tool. See `docs/ACCEPTANCE_SCENARIOS.md` for runtime test expectations.

For routing precedence, evidence and approval details, follow `docs/ORCHESTRATOR_EXECUTION_CONTRACT.md`. For current platform guidance use `docs/PLATFORM_EVIDENCE_REGISTER.md`; do not promise engagement growth or assume live social-network access.
