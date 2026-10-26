---
name: post-qa
description: "Apply final per-platform, evidence, voice, accessibility, rights and approval-readiness checks to drafted posts and assets."
---

# Post Qa

**Purpose.** A consistent pass/revise/blocked verdict that actually protects quality.

**Trigger and ownership.** Final stage after a writer/editor, before presenting for human approval or delivery.

**Inputs.** Complete copy, sources and fact-check ledger, selected platform/format, asset paths or honest missing flags, user preferences.

## Required process

1. Confirm request adherence: exact format, number of posts, audience promise, content pillar and useful specific takeaway.
2. Gate factual assertions: no missing source for material claims, fake biography, invented testimonials, brand statistics or algorithm guarantees.
3. Gate platform requirements: up-to-date length/media rules checked where applicable, natural readability and relevant CTA only.
4. Gate assets: actual file exists and was inspected; descriptions and alt text correspond to what was produced; storyboard-only output stays blocked for image publication.
5. Check copyright, accessible language, inclusive presentation and absence of misleading engagement manipulation.
6. Distinguish **editorial quality score** (subjective internal review) from **measured performance** (observed analytics). Never predict reach from a score.
7. Return `pass_for_user_review`, `revise` with exact fixes, or `blocked` with unmet hard gates. Final user approval is separate from QA.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Explicit verdict, failing criteria with repair instructions, final content and outstanding human approvals.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

QA passing never means user approved or externally scheduled; not a substitute for real account analytics.

## Acceptance tests

- Unsupported fact blocks.
- missing image blocks visual publishing.
- real user review still required.
- edits retested.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
