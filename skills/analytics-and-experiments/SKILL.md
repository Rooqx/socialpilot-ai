---
name: analytics-and-experiments
description: "Analyze actual cross-platform post performance and design measured improvements without inventing metrics or causal certainty."
---

# Analytics And Experiments

**Purpose.** Reproducible observations, hypotheses and properly scoped experiments.

**Trigger and ownership.** When user supplies exports, asks what performed well, or requests A/B-style content improvement.

**Inputs.** CSV/JSON/verified API export, platform and observation period, post IDs, metric definitions, account goals and sample sizes.

## Required process

1. Verify data provenance, freshness and fields. If no data source exists, say analytics cannot be computed and offer a template.
2. Normalize post-level metrics by platform and time period, recording denominators and measurement window. Avoid comparing raw views across incomparable metrics.
3. Summarize actual reach, engagements, relevant replies, saves, follows or conversions available; never invent missing metrics.
4. Group by topic, format, hook and time with sample-size caveats. Distinguish description, correlation and plausible cause.
5. Track posts in a content-family hierarchy so repurposed variants are not double-counted as independent concepts.
6. Suggest a small number of falsifiable next tests: change one meaningful variable, set a primary metric, stop condition and reporting window.
7. Pass only evidence-backed learnings to `continuous-improvement`, with dates, confidence and expiration/retest conditions.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Observed-metrics table, caveats, best/worst contextual examples, falsifiable experiments, and missing-data report.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Never show mock dashboards as real account analytics or interpret tiny samples as certain causal results.

## Acceptance tests

- Empty data yields no fake graph.
- missing denominator flagged.
- test has hypothesis, metric, period and stop rule.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
