# Antigravity / Gemini agent entry

Read `AGENTS.md` and the canonical `.agents/skills/social-orchestrator/SKILL.md` first for requests like “start posting”. Recover state via `python3 scripts/socialctl.py status`, then load only requested capabilities from `.agents/skills/`. Before posting, sending, or changing any connected account, ask for explicit authorization. The checked-in files are guidance, not proof that this runtime's native skills feature automatically discovers the folder. Confirm actual discovery in a fresh runtime test.

**Specialist loading (v0.3):** After selecting a skill, read its `references/playbook.md` and `references/field-manual.md` for detailed domain decisions, methods, and worked examples. Read `references/source-fidelity.md` when auditing provenance. Load playbooks **only for selected skills**; do not eagerly load all 28. Use `scripts/route_preview.py` only as a dry-run route diagnostic, never as evidence that an AI agent has actually chosen or executed a tool. See `docs/ACCEPTANCE_SCENARIOS.md` for runtime test expectations.

For routing precedence, evidence and approval details, follow `docs/ORCHESTRATOR_EXECUTION_CONTRACT.md`. For current platform guidance use `docs/PLATFORM_EVIDENCE_REGISTER.md`; do not promise engagement growth or assume live social-network access.
