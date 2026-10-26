---
name: idea-pipeline
description: "Capture, deduplicate, evaluate and prioritize social content ideas from lived experience, research and user requests."
---

# Idea Pipeline

**Purpose.** A living backlog that grows from evidence and avoids repeated generic posts.

**Trigger and ownership.** When asked what to post, after research, or when a new project update/event arrives.

**Inputs.** Current pillars and audience, source opportunities, existing backlog, fresh creator anecdotes if confirmed.

## Required process

1. Intake raw seeds with origin (user project, question, source research, analytics, listening, customer story) and receipt/source.
2. Expand each seed into distinct audience-specific angles, not superficial paraphrases. Include contrarian alternatives only when defensible.
3. Score qualitatively on relevance, novelty, credibility, timeliness, available proof, effort and format fit; report assumptions, not numerical predictions of virality.
4. Deduplicate against the idea index and published history using topic and central claim, not exact string matches alone.
5. Assign a stable key, pillar, primary platform, preferred format, evidence requirements and next owner action.
6. Select a balanced queue; defer ideas whose factual support or personal story is missing instead of inventing them.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Prioritized backlog entries with angles, evidence gaps, formats, status and idempotency keys.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Never generate a fake personal anecdote to fill a slot; no recycled identical platform posts.

## Acceptance tests

- Duplicate rejected.
- missing proof becomes blocked.
- prioritized backlog has traceable reasons.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
