---
name: x-post-writer
description: "Draft natural, concise single X posts with a grounded insight and audience-appropriate voice."
---

# X Post Writer

**Purpose.** A complete X post that makes one useful point, not a LinkedIn essay squeezed into a tweet.

**Trigger and ownership.** When user asks for a tweet, X post or X-specific concise observation.

**Inputs.** Verified angle, author voice, source facts, optional media and current length constraints.

## Required process

1. Read confirmed identity and voice; extract one main idea and what makes it credible. Ask about a missing personal claim rather than fabricating.
2. Choose a native form: observation, lesson, practical tip, brief story, insightful question or response to a source.
3. Lead with useful specificity; remove throat-clearing, synthetic drama, hashtags for decoration and excessive link stuffing.
4. Draft concise text with sensible line breaks; if the point cannot fit without losing essential nuance, ask to use `x-thread-writer`.
5. For numbers, quotes, current events and code facts attach exact evidence for `fact-checker`. Use technical terms correctly.
6. Count Unicode characters conservatively and validate against current official account constraints before handoff; avoid relying on an assumed premium-account limit.
7. Run facts → voice/clarity → QA. Present copy as a draft, never imply it was posted.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

One copy-ready X post, optional alternate hook, source notes if relevant, exact measured length, QA state.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No unsupported algorithm-rank claims, fabricated personal events, or template padding.

## Acceptance tests

- Post fits verified limit.
- central claim clear.
- zero fake proof.
- link/hashtag intentional.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
