# Rolling calendar with revision safety

## A calendar is a stateful queue

A slot needs `slot_id`, intended platform, format, pillar, family key, brief/draft ID, owner, target window with timezone, asset dependency, fact-check status, approval status and externally confirmed scheduling status **if any**. A planned slot is not a scheduled post. Keep existing rows across sessions and append or amend only what is necessary.

## Weekly update procedure

1. Read the current calendar and draft index. Partition entries into published/report-confirmed, approved, review-pending, production-blocked and unfilled.
2. For "posts this week," calculate *only the open gap*. Do not include a completed draft twice or silently recreate a previously rejected idea.
3. Allocate capacity based on writing/visual effort, source availability and the creator's real schedule. Never assert that a specific posting hour guarantees success.
4. Place dependencies before delivery: interviews, screenshots, citations, design, accessibility review and approval must have feasible lead time.
5. Propose a small delta: reused items, moved items, new slots, still blocked, and rationale. Obtain agreement before changing previously approved entries.
6. Use offset-aware local times; fail closed on ambiguous times or unknown locale when required.

## Worked scenario

Request: "Prepare five posts this week." Existing queue has two QA-passed drafts awaiting approval, one approved Instagram carousel without rendered visuals and one blank slot. Do not write five new pieces. Surface the two reviews; flag the visual dependency; propose one verified topic for the empty slot; ask whether the user wants additional volume after accounting for existing work.

## Validation

No duplicate `draft_id`, no silent status promotion, no unauthorized scheduling claims, no plan that assumes unconfirmed media is ready. If the user asks to move an approved post, retain the approval for **unchanged copy** but still confirm timing and destination before any actual external action.
