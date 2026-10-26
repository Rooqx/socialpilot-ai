---
name: audience-research
description: "Investigate an audience’s real questions, jobs-to-be-done, vocabulary, objections and content needs using attributable evidence."
---

# Audience Research

**Purpose.** An actionable audience brief grounded in observed behavior rather than fictional personas.

**Trigger and ownership.** New niche, shifts in audience, low-performing themes or requested audience investigation.

**Inputs.** Explicit niche and audience hypotheses; accessible community/review/interview sources; research dates.

## Required process

1. Specify research question, target platform, geography/language only if relevant, and what counts as audience evidence.
2. Use consented interviews, publicly available discussions, FAQs, reviews or user-provided materials; preserve source URL, date and quotation context.
3. Extract recurring jobs/problems, language patterns, frequent questions, technical sophistication and competing approaches.
4. Separate observations from hypotheses; do not extrapolate a few noisy social posts to a whole population. Mark sample size and selection bias.
5. Map themes to content opportunities and the platform audiences likely to benefit, including counterexamples and underserved segments.
6. Produce a ranked evidence matrix, not synthetic demographics. Flag privacy, source terms of service, and freshness limitations.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Audience theme matrix (claim, example, source, strength, confidence), audience hypotheses, content questions and known gaps.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No private scraping or fabricated quotes/personas; no unsupported assertion that a topic is trending.

## Acceptance tests

- Zero sources stays hypothetical.
- private content excluded.
- sample sizes included.
- source dates recorded.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
