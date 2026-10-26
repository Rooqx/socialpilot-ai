# Professional narrative playbook

## Select a defensible narrative

| Source material | Strong structure | Critical risk |
|---|---|---|
| Real implementation choice | Context → options → tradeoff → decision → caveat | Invented benchmarks |
| Verified learning | Prior assumption → evidence → revised approach → reader takeaway | Performing expertise without evidence |
| Public product update | What's changed → why it matters → who benefits → next step | Fabricated customers or launch status |
| Technical guide | Situation → reproducible steps → common failure → check | Oversimplification that changes code meaning |

## Drafting discipline

1. Determine the actual reader (peer engineer, recruiter, potential client, founder). That changes jargon, stakes and necessary context.
2. Obtain project-specific facts from the creator or accessible repository; don't quietly convert a hypothetical demo into a personal achievement.
3. Write the substantive insight before the first line. The opening should communicate why this particular example matters.
4. Use complete natural sentences. Break paragraphs for readability, not a formula of one or two words per line.
5. Show an *actual* tradeoff or verified detail, including limitations; avoid performance numbers and customer counts unless sourced.
6. Close at the point of useful conclusion. Do not force a sales pitch or empty engagement question.
7. Recheck factual meaning after edits and current platform limits at handoff.

## Example (hypothetical, not user biography)

Weak: "Consistency is the secret to success in software engineering." More useful: "An API timeout isn't automatically a failed transaction. When the client retries, you need to decide whether the operation is safe to repeat. For payments and other side effects, an idempotency key can be the difference between recovery and duplicate work." If tied to a personal project, the exact implementation must be confirmed.

## Review protocol

Is there a concrete example? Would someone who didn't know the author learn something? Are caveats honest? Does the post sound like this author, rather than generic career content? Has the agent mixed up a document carousel with an ordinary feed post? Record questions rather than inserting invented answers.
