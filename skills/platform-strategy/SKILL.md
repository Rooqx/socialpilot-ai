---
name: platform-strategy
description: "Maintain current, evidence-qualified differences among organic X, Instagram and LinkedIn content formats and constraints."
---

# Platform Strategy

**Purpose.** Platform-native output without static myths about algorithms or obsolete character/image limits.

**Trigger and ownership.** Before platform-specific content or when platform mechanics affect the format.

**Inputs.** Target platform, post format, current official platform documentation where accessible, audience and creative format.

## Required process

1. Identify X short post/thread, LinkedIn feed/document/article, or Instagram feed/carousel/Reel/Story explicitly; they differ in capabilities and visibility.
2. Load the relevant platform authoring guide from `docs/platform-playbooks.md`. Check mutable length, ratio, media and accessibility limits against official documentation at execution if publication depends on them.
3. Prioritize useful stories, credible examples, clear intent and accessible presentation rather than mechanistic ranking tricks.
4. Apply culturally appropriate voice and CTA: a useful conversational exchange on X, professional evidence on LinkedIn, and visual-first narrative on Instagram.
5. Mark platform constraints `verified_at` and `needs_refresh`, and pass only validated requirements to `post-qa`.
6. Avoid universal timing, hashtag or algorithm multipliers; treat observed results as account-specific hypotheses.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Per-platform execution brief with format, audience promise, creative needs, checks and mutable constraints marked verified or unverified.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Never declare precise rank penalties or preferred posting times without solid, current evidence.

## Acceptance tests

- Three platform distinctions recognized.
- volatile requirements do not hard-code promises.
- missing verification flagged.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
