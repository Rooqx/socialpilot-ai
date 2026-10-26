---
name: community-engagement
description: "Draft helpful public replies and comment strategies for X, LinkedIn and Instagram without spam, manufactured interaction or unsolicited outreach."
---

# Community Engagement

**Purpose.** Genuine conversations that advance the topic and respect the creator’s voice.

**Trigger and ownership.** When user asks for replies, discussion prompts, first comments, comment triage or networking suggestions.

**Inputs.** Original public post and source, author expertise, relationship context, platform, approved boundaries.

## Required process

1. Read exact post context; determine whether a reply adds a fact, constructive question, lived insight or useful resource.
2. For X keep concise and conversational; LinkedIn can include a grounded professional observation; Instagram should relate directly to media/caption.
3. Avoid generic compliments, repetitive templates, engagement pods, rage bait, impersonation and mass outreach.
4. Verify any technical/factual additions; if uncertain, ask or phrase as a genuine question.
5. Present a small set of optional drafts sorted by relevance and effort, with URL/context and no claims that they were posted.
6. Require explicit user authorization before sending comments or DMs; respect moderation rules and creator boundaries.
7. Record which responses the user used only when confirmed, to prevent repeated messages.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Optional reply drafts, rationale, source context, constraints and manual engagement checklist.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No bulk posting or unauthorized outreach; no sensitive or private thread scraping.

## Acceptance tests

- Reply adds value.
- original meaning understood.
- authorization gate holds.
- repeated suggestion deduplicated.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
