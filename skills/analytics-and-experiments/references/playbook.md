# Measurement protocol and honest comparisons

## Each metric needs a denominator and window

Store platform, post ID, source, observation timestamp, publication timestamp, metric definitions and measurement window. Distinguish **impressions, reach, views, plays, interactions, saves, followers** and externally tracked conversions; they are not universally interchangeable. Cross-platform raw counts can mislead because platforms define them differently.

## Repeatable analysis

1. Validate file format and source. Reject negative counts, nonnumeric fields and invented values.
2. Group post variants by family key without double-counting an insight as separate independent campaign outcomes.
3. Choose comparable windows (e.g. first 48 hours *where data exist*) and avoid comparing a new post with a six-month-old one without qualification.
4. Compute rates only with a documented denominator; display numerator and denominator alongside the rate.
5. Identify recurring *observations*: format, topic, opening, publishing context; do not infer platform algorithm causation from a tiny sample.
6. Propose experiments with specific hypotheses, primary metrics, sample adequacy considerations, a stop condition and a comparison plan.
7. Separate account access limitations, missing fields and confidence in every finding.

## Example

Post A has 12 saves and 300 observed impressions; Post B has 20 saves and 1,000 impressions. If both measurements mean the same thing and share comparable windows, save rates are 4% and 2% respectively. That supports a description of this sample—not a claim that A is universally twice as effective or that its hook caused the difference.

## Failure tests

No export available; impressions defined differently; sampled posts from different date windows; bot activity not identifiable; only two examples; confounding of topic and format; an imported figure with no source. Return an explicit missing-data plan instead of fabricated benchmarks.
