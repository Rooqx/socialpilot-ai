---
name: context-manager
description: "Initialize, reconcile, and maintain persistent author identity, audience facts, preferences, project context, and decision provenance across agents."
---

# Context Manager

**Purpose.** One authoritative identity and fact record, separate from volatile task state and inferred writing voice.

**Trigger and ownership.** On first setup, when identity facts change, when authorship or project facts conflict, or when a skill lacks grounding.

**Inputs.** `.social/profile.json`, `.social/strategy.json`, optional verified links and user-confirmed notes; source and verification timestamp.

## Required process

1. Read existing records before asking anything. Distinguish empty placeholders from confirmed values.
2. Capture identity, account type, platforms, audience, goals, niche, confirmed projects, topics to avoid, location-sensitive claims, and contact details only if relevant and volunteered.
3. Annotate material facts with `value`, `source_type`, `source_ref`, `verified_at`, and `confidence` (`user_confirmed`, `verified_source`, `unverified`). Never import upstream example authors or public profiles as the current user's biography.
4. If new information contradicts saved facts, preserve both in `conflicts` and request clarification before assertions depend on it. Never silently overwrite a material fact.
5. Save through atomic state updates or carefully edited structured files; keep auth secrets out of markdown and Git. Prefer `.social/` local-private state; export sanitized profiles only intentionally.
6. Separate durable knowledge (identity, voice principles, pillar choices) from operations (draft status, last run, approvals). Track decisions with date and rationale.
7. On next invocation, reuse confirmed facts rather than repeating onboarding. Surface missing minimum inputs only.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Updated profile/strategy, provenance on material facts, unresolved conflicts, and a concise `known vs missing` summary.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Never infer follower counts, achievements, client names, age, income, or private data; do not put personal profiles into public sample files.

## Acceptance tests

- Conflicting biography blocks fabrication.
- clean restart restores facts.
- old project defaults cannot impersonate user.
- credentials excluded.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
