---
name: linkedin-post-writer
description: "Write evidence-based, professionally credible LinkedIn feed posts in the author’s natural voice."
---

# Linkedin Post Writer

**Purpose.** Professional insight and authentic experience, not corporate boilerplate or fabricated achievements.

**Trigger and ownership.** When user requests LinkedIn post, developer learning, project case study or professional opinion.

**Inputs.** Actual project/story facts, audience, purpose, voice, credible proof and desired format.

## Required process

1. Separate what the author did, noticed and believes from unconfirmed claims. Pull project details only from sources genuinely available.
2. Choose one useful narrative: a tested lesson, trade-off decision, before/after with real data, breakdown, mistake and remedy, or teaching post.
3. Write a first line with stakes and specificity; use natural paragraphs and only as much whitespace as improves readability.
4. Show concrete actions, alternatives, outcomes and caveats. Never invent employer, promotion, client numbers or performance results.
5. Distinguish feed text from LinkedIn document/carousel posts: for slide structure route to `carousel-storyboard` and keep copy matched.
6. End with a thoughtful observation or optional authentic question, not compulsory "agree?" engagement bait.
7. Confirm current length/accessibility constraints, check claims, copy edit against voice profile, and label as a draft.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Copy-ready LinkedIn post, intended audience, source check, optional document brief and QA status.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No generic inspirational claims masquerading as personal experience; no fake professional social proof.

## Acceptance tests

- Unverified achievements held.
- voice recognizably author-specific.
- substantive insight.
- readable format.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
