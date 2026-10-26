# Thread architecture and continuity checks

## When to choose a thread

Use an ordered thread for multi-step procedures, evidence with necessary context, case studies or competing tradeoffs. A thread with one substantive item and repeated teasers should collapse into a single post.

## Architect before drafting

1. State the outcome the reader should understand by the end; outline at most one central argument.
2. Make post 1 promise a concrete payoff and clearly signal the topic without fake cliffhangers.
3. Write each interior item as one independent advance: definition, problem, example, counterexample, remedy or verification step.
4. Give links, code snippets and numbers only when sources or user-confirmed materials actually support them.
5. Use explicit causal transitions where needed; avoid "and then something wild happened" padding. A screenshot description is not proof the screenshot exists.
6. End with a short synthesis. Include an optional authentic question only if it opens a useful discussion.
7. Check every item individually for current platform restrictions, and then check the thread as a whole for repeated claims, contradictions and missing bridges.

## Example outline

Topic: resilient webhooks. 1: problem and outcome; 2: why retries occur; 3: duplicate delivery; 4: idempotency-key boundary; 5: ordering/timeout considerations; 6: operational check; 7: summary. This is an outline, not a claim that the author personally ran any experiment.

## Adversarial checks

Swap two middle posts and ask whether it remains understandable. Remove the opening and inspect whether the technical content still makes sense. Check for a statistic introduced in one post and contradicted later. Ensure all 7 parts still tell the *same* story and no link or media asset is merely presumed to exist.
