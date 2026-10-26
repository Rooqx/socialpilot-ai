# Evidence-led improvement and controlled promotion

## Separate three categories

**Owner preference:** explicit instruction about tone or format; may update brand/voice rules after confirmation. **Observed pattern:** several comparable measured posts or a documented experiment; can inspire a provisional hypothesis. **System defect:** a skill instruction causes reproducible routing, factual or state failures; warrants a tested fix. These categories have different proof burdens.

## Learning lifecycle

1. Read previous run logs, decisions and known experiments before introducing changes.
2. Identify what changed and its potential causes. Check whether the problem was lack of data, missing context, tool failure or poor writing.
3. Record `observation`, `supporting_runs`, `confidence`, `scope`, `proposed_rule`, `risk`, `review_date` and `rollback_condition`.
4. Seek owner approval to promote a durable voice or strategy rule. Never allow an autonomous loop to rewrite root instructions without review.
5. For a code/skill fix, add an explicit regression test, update only the necessary skill and rerun adapter checks.
6. Retain old versions and explain reversal conditions. Do not claim learning from analytics you never received.

## Worked example

In three comparable posts, audience comments repeatedly request diagrams. Valid learning: *test diagram-supported posts on this topic*. Invalid learning: *Instagram now favors diagrams by exactly 200%* or *all future posts must be carousels*. Run a small experiment, track outcomes and let the creator decide whether it becomes a guideline.

## Loop guardrails

No self-awarded QA pass, auto-publication, covert account changes, or monitoring promises without an actual scheduler. Duplicate or contradictory learnings should be reconciled with evidence, not resolved by whichever file was edited most recently.
