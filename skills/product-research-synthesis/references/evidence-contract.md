# Evidence contract

## Evidence classes

### `EVIDENCE`

A directly observed item from a supplied source.

Quantitative evidence records:

- source file/query;
- metric definition;
- numerator and denominator when applicable;
- segment;
- time window and timezone;
- sample size;
- value and comparison;
- data-quality caveats.

Qualitative evidence records:

- participant or artifact ID;
- segment when known;
- source file and locator;
- exact quote or faithful observation;
- descriptive tag;
- whether the observation is prompted or spontaneous.

### `USER_BELIEF`

Anything supplied as the author's thought, explanation, expectation, fear,
preference, or interpretation. It may become a hypothesis, but it is not
evidence for itself.

### `MODEL_INFERENCE`

A pattern name, mechanism, causal candidate, implication, or recommendation
derived from evidence. It must list supporting and opposing evidence IDs.

## Required record shape

Use one compact record per atomic observation:

```json
{
  "id": "E-Q-001",
  "class": "EVIDENCE",
  "source_type": "quant|interview|note|experiment|context",
  "source_file": "input/quantitative/funnel.csv",
  "locator": "row/filter/page/timestamp",
  "participant_id": null,
  "segment": "new mobile users",
  "claim": "Activation fell from 31% to 24%.",
  "value": {"before": 0.31, "after": 0.24, "n": 1834},
  "quote": null,
  "tags": ["activation", "mobile"],
  "confidence": "MEDIUM",
  "notes": "Tracking schema changed two days earlier."
}
```

IDs:

- `E-Q-*` quantitative evidence;
- `E-I-*` interview/qualitative evidence;
- `E-X-*` experiment evidence;
- `B-*` user beliefs;
- `H-*` hypotheses;
- `F-*` synthesized findings;
- `GAP-*` gaps;
- `GOAL-*` goals.

## Qualitative discipline

- Code each artifact before clustering across artifacts.
- Count distinct participants, not repeated statements by one participant.
- Keep dissent and counterexamples.
- Do not infer prevalence from a convenience sample.
- A single participant is an anecdote.
- Two independent participants are an emerging signal.
- Three or more independent participants may be called a pattern only when the
  sample and segmentation make that interpretation defensible.
- Frequency is not severity. A rare blocker may outweigh a common annoyance.
- Interview statements describe reported experience; they do not automatically
  prove observed behavior.

When a routed upstream method sets a stricter threshold, follow it.

## Quantitative discipline

- Define the unit of analysis before calculation: user, account, session, event,
  order, or revenue.
- Inspect missingness, duplicates, bot/internal traffic, identity stitching,
  schema drift, timezone, late events, and selection/filtering.
- Compare like periods and like segments.
- Report denominators and uncertainty.
- Check aggregate and segment-level behavior to avoid mix-shift errors.
- Do not explain a metric with the same metric restated in different words.

## Finding standard

A finding contains:

1. one falsifiable claim;
2. evidence for;
3. evidence against or a statement that none was found;
4. relationship type:
   `CONVERGENT`, `COMPLEMENTARY`, `CONTRADICTORY`, `SEGMENTED`,
   `TEMPORALLY_DIFFERENT`, or `UNRESOLVED`;
5. confidence: `LOW`, `MEDIUM`, or `HIGH`;
6. product implication labeled as `MODEL_INFERENCE`;
7. open questions.

## Hypothesis status

Use exactly one:

- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `CONTRADICTED`
- `MIXED`
- `INSUFFICIENT_EVIDENCE`
- `NOT_TESTED`
- `SUPERSEDED`

Preserve the original statement. Put improved wording in a separate
`revised_statement`; never rewrite history.

## Confidence

- **HIGH**: multiple independent evidence sources or robust data views agree,
  quality checks pass, and no major unresolved contradiction remains.
- **MEDIUM**: one strong source plus partial triangulation, or multiple weaker
  sources with manageable caveats.
- **LOW**: sparse or biased sample, weak measurement, unstable estimate,
  unresolved contradiction, or an inference that has not been tested.

Confidence describes support for the claim, not enthusiasm for the idea.

## Causality

Use `associated with`, `consistent with`, or `may explain` for observational
patterns. Use `caused` only after an experiment or a defensible identification
strategy. Never turn chronology alone into causality.

## Gaps

Classify each gap as one of:

`DATA`, `MEASUREMENT`, `QUALITATIVE_COVERAGE`, `CAUSALITY`, `DECISION`, `GOAL`,
`CONTRADICTION`, `RECENCY`, or `EXPERIMENT`.

Each gap needs decision impact, priority, and the smallest next action that can
close it.
