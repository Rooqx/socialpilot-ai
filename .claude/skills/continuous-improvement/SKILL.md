---
name: continuous-improvement
description: "Run an evidence-driven postmortem and update durable lessons, task checkpoints and experimental changes after content work."
---

# Continuous Improvement

**Purpose.** Self-improvement through recorded evidence, not imagined performance or silent background behavior.

**Trigger and ownership.** After content delivery, measured results, user feedback, failed QA or a request to review system quality.

**Inputs.** Run log, QA outcomes, actual analytics and human feedback, current strategy assumptions and active experiments.

## Required process

1. Recover previous decisions and experiment outcomes before recommending a new change.
2. Compare what was planned, delivered, blocked and confirmed by evidence; identify root causes, not generic platitudes.
3. Promote to durable guidelines only repeatable patterns supported by actual data or explicit owner direction; mark confidence and original source.
4. Record a learning with evidence id, affected skill/format, precise rule change, owner approval status and review date.
5. Keep run-level deviations in log and rollback any experiment that fails the predeclared safety or outcome threshold.
6. Define next review triggers; do not promise recurring monitoring unless a real scheduled automation is configured.
7. Distinguish defects in skill instructions from normal editorial taste, and propose narrowly scoped revisions with tests.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Change proposal or learning entry, supporting observations, owner decision, revisit criteria and next run checkpoint.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No circular self-certification; never upgrade a hypothesis to platform fact from one successful post.

## Acceptance tests

- Unsupported learning remains tentative.
- repeated failures trigger revision.
- no background task claimed.
- approvals preserved.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
