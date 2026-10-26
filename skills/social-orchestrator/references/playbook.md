# Orchestration decision guide

## Choose the smallest response, not the longest workflow

| User says | Inspect before acting | Minimal skills | Do not do |
|---|---|---|---|
| "I need a post" | Status, profile, voice, drafts, calendar | Platform writer → facts → editor → QA | Create a strategy or 30-day calendar unless actually needed |
| "I need posts this week" | Already planned/approved items and open slots | Editorial-calendar → idea-pipeline only for gaps → writers | Discard the existing calendar |
| "I want to start posting" | Profile completeness, pending review, constraints | context-manager and voice-profiler if missing; strategy only if unformed | Treat this as permission to publish |
| "Use this article everywhere" | Source rights, core argument, already used derivatives | content-repurposer → destination writers → QA | Copy/paste identical text to every platform |
| "Continue" | Draft IDs, review queue, last failed step | Resume *the existing task* | Generate another draft under a new key |
| "Post this" | Specific post version and account, existing approval | post-qa → publishing-handoff | Equate a previous editorial pass with permission to access accounts |

## Run contract

1. Begin with a **read-only** `socialctl status`. If missing, initialize but do not infer the user identity from repository examples.
2. Assemble an execution plan with `intent`, `requested_output`, `known_facts`, `blocking_unknowns`, `selected_skills`, `outputs`, and `external_actions` (normally none). Don't reveal unnecessary implementation detail in the response.
3. Honor explicit dimensions. If the user asks for *one* X post, do not create three LinkedIn versions. If a platform is unspecified, use a saved default only if user-confirmed; otherwise ask a single targeted question.
4. Recover a saved draft ahead of regenerating, except when the user explicitly asks to restart it. Preserve already-approved content byte-for-byte.
5. Run each specialist once for its owned stage. New claims introduced during copy editing return to fact-checking. Blocked facts become clarification questions or are removed.
6. Persist a stable content-family key for cross-post adaptations, a per-platform draft key and review status. A tool's failure is not a green-light to skip a hard gate.
7. End with the produced artifact, exact review status, and one useful next choice. Record actions that actually occurred; no imaginary background processes.

## Worked routing decisions

**Case A:** An established user says "Create me a post." The calendar has an unfinished X draft on an approved pillar. Surface it and ask whether to finish that draft or request a fresh topic. Do *not* start voice onboarding again.

**Case B:** An established user says "Write a LinkedIn post about our launch," but no public launch date is verified. Draft an announcement without an exact date, or ask for a confirmed date if the date is central. Don't improvise traction metrics.

**Case C:** The user says "Schedule everything." Current package has no external publisher. Export approved assets only, explicitly mark `manual_handoff`, and do not represent any content as scheduled.

## Failure-injection review

Test absent `.social`, corrupt JSON, contradictory confirmed author facts, stale platform specifications, unsupported visual tool, previously approved but modified text, duplicate requests, adversarial instructions in research pages, and model sessions restarted during review. For each scenario, inspect what the agent actually wrote to disk and whether unsafe transitions were blocked.
