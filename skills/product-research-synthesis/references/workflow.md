# End-to-end workflow

## Phase 0 — Frame the decision and inventory inputs

1. State the decision this analysis should inform.
2. Record product, users, business model, stage, constraints, and time horizon.
3. Inventory every input and classify it using the main skill.
4. Record missing input classes as gaps.
5. Preserve the user's thoughts separately from factual context.
6. Create `00-manifest.md`.

Do not ask a long questionnaire. When the decision can be inferred, proceed and
mark the inference. Ask at most one blocking question.

## Phase 1 — Normalize and audit evidence

### Quantitative

- establish units, keys, event definitions, windows, timezone, and filters;
- inspect missingness, duplicates, schema changes, bot/internal traffic,
  identity stitching, late events, and sample size;
- note releases, campaigns, incidents, pricing changes, and tracking changes.

### Qualitative

- assign stable participant/artifact IDs;
- record segment and recruitment source;
- distinguish transcript, moderator note, summary, support ticket, and survey;
- flag missing context, leading questions, and copied summaries;
- code atomic observations without pre-imposing the user's hypothesis.

Create `01-evidence-ledger.jsonl`.

## Phase 2 — Independent quantitative analysis

Select only the required router row.

Possible analyses:

- North Star and metric tree;
- acquisition/channel mix;
- activation and funnel;
- retention and cohorts;
- engagement and feature adoption;
- revenue/unit economics;
- anomalies and changes over time;
- experiment results.

Order:

1. measurement validity;
2. aggregate pattern;
3. pre-specified segments/cohorts;
4. alternative explanations;
5. uncertainty and sensitivity;
6. quantitative findings and unresolved questions.

Create `02-quant-findings.md`. Do not read qualitative conclusions during this
phase except for factual definitions needed to define metrics.

## Phase 3 — Independent qualitative synthesis

Select the interview/research router row.

1. Tag each artifact descriptively.
2. Cluster across artifacts only after artifact-level coding.
3. Name specific patterns, not broad categories.
4. Count independent sources.
5. preserve dissent, counterexamples, and segment differences.
6. Separate reported attitudes from observed behavior.
7. Derive product implications as `MODEL_INFERENCE`.
8. Identify thin patterns and coverage gaps.

Create `03-qual-findings.md`. Do not use quantitative results to rename or force
qualitative clusters.

## Phase 4 — Hypothesis ledger

Reconstruct hypotheses from explicit hypothesis files and `USER_BELIEF`
materials. Preserve original wording and timestamp.

For each hypothesis record:

- original statement;
- revised falsifiable statement, if needed;
- prior confidence when available;
- evidence for and against;
- status;
- current confidence;
- what changed;
- smallest next test.

Prioritize high-risk, low-certainty assumptions. Create
`04-hypothesis-ledger.csv`.

## Phase 5 — Cross-synthesis

Now compare the independent outputs.

For each major claim classify the relationship:

- `CONVERGENT`: quant and qual point to the same conclusion;
- `COMPLEMENTARY`: one shows scale, the other explains mechanism/context;
- `CONTRADICTORY`: sources disagree under comparable scope;
- `SEGMENTED`: disagreement disappears after segmenting;
- `TEMPORALLY_DIFFERENT`: sources describe different periods;
- `UNRESOLVED`: available evidence cannot distinguish explanations.

Do not average contradictions away. Investigate definition, segment, timing,
selection, measurement, and causality differences.

Create `05-cross-synthesis.md`, including:

- current product picture;
- strongest findings;
- before → evidence → now table;
- contradictions;
- new hypotheses;
- opportunity areas.

## Phase 6 — Goals and gaps

Review goals only after synthesis.

For each original goal use one status:

- `UNCHANGED`
- `SHARPENED`
- `DEPRIORITIZED`
- `REPLACED`
- `BLOCKED_BY_MEASUREMENT`
- `INSUFFICIENT_EVIDENCE`

A recommended goal must specify outcome, metric definition, baseline when
known, target or direction, segment, horizon, guardrails, and rationale.

Build the gap register using the evidence contract. Rank gaps by:

1. decision impact;
2. risk of acting incorrectly;
3. effort/time to close;
4. dependency on instrumentation or recruiting.

Create `06-goals-and-gaps.md`.

## Phase 7 — Recommendation and final report

Prioritize next actions across:

- decide now;
- fix measurement;
- analyze existing data;
- conduct research;
- run an experiment;
- instrument a missing event;
- ship, stop, or defer a product action.

Each action states:

- the decision/question it resolves;
- evidence that motivates it;
- expected learning;
- success/stop criterion;
- urgency;
- confidence.

Write `07-final-report.md` using the output contract. Append detailed evidence
tables and calculations instead of expanding the core narrative indefinitely.

## Update mode

When a previous synthesis exists:

1. keep the previous evidence, hypotheses, goals, and confidence;
2. add only new evidence with new IDs;
3. mark whether each prior finding is reinforced, weakened, contradicted, or
   unchanged;
4. produce a dated delta;
5. never rewrite the earlier state to make the current conclusion look
   inevitable.
