---
name: product-research-synthesis
description: End-to-end, evidence-first product research synthesis across raw quantitative data, interview transcripts, research notes, project context, the user's own thoughts, existing hypotheses, goals, and experiment results. Use when the user wants a broad product assessment: what the evidence says, where sources agree or conflict, which hypotheses remain supported, what changed, what is still unknown, how goals should be revised, and what to investigate or test next. This is a token-aware orchestration skill: it progressively loads pinned upstream methods instead of preloading a monolith.
---

# Product Research Synthesis

Produce a decision-grade product understanding from mixed evidence without
confusing observations, the user's beliefs, and model inference.

## Start here

Read these local references before analysis:

1. `references/evidence-contract.md`
2. `references/router.md`
3. `references/token-budget.md`
4. `references/workflow.md`
5. `references/output-contract.md`

Use `SOURCES.lock.json` as the authority for upstream repository, commit, license,
and path. Prefer the local submodule path. If a submodule is unavailable, fetch
the exact file from the named GitHub repository at the pinned commit.

## Non-negotiable rules

1. **Keep evidence classes separate.**
   - `EVIDENCE`: directly observed in supplied data or source material.
   - `USER_BELIEF`: the user's thoughts, interpretations, expectations, or
     preferred explanations.
   - `MODEL_INFERENCE`: an interpretation derived by the model.
   Never promote one class to another.

2. **Do not rewrite upstream rules.** Load and apply the original routed file
   within its scope. This orchestrator selects order and scope only. When
   upstream methods disagree, state the conflict and preserve both positions;
   do not silently blend them into a new rule.

3. **Trace every material claim.** A finding must point to evidence IDs and
   source locators. A quantitative claim needs metric definition, denominator,
   time window, and segment. A qualitative claim needs participant or artifact
   IDs and recurrence across independent sources.

4. **Analyze sources independently before cross-synthesis.** Do not read the
   user's preferred explanation and then code interviews or data to fit it.
   Quantitative, qualitative, hypotheses, and goals each receive a separate
   pass before they are compared.

5. **Check measurement before meaning.** Tracking changes, missing data,
   duplicates, identity problems, schema drift, selection bias, and sample size
   can invalidate downstream interpretation.

6. **Do not turn association into causation.** Observational evidence may support
   an association or mechanism hypothesis. Causal language requires an
   experiment or an explicit identification strategy.

7. **Name uncertainty and missing evidence.** `INSUFFICIENT_EVIDENCE`,
   `NOT_TESTED`, and `UNRESOLVED` are valid outcomes. Absence of evidence is not
   evidence against a hypothesis.

8. **No invented insights or quotes.** Quotes must be exact and locatable.
   Single-source qualitative observations stay anecdotes unless a routed
   upstream method explicitly supports another classification.

## Choose the run mode

- **full** — mixed raw data plus interviews/notes, or a request for a broad
  product assessment. Run all relevant phases.
- **update** — a prior synthesis exists and new evidence must be compared with
  it. Preserve old hypotheses and goals; add a dated delta.
- **focused** — one bounded question. Run only the phases required to answer it,
  but still apply the evidence contract.

Choose `standard` depth unless the user names another level. A request for a
"полный", "широкий", or "deep" analysis selects `deep`, while still following
the same progressive-loading limits.

## Intake classification

Classify every input before interpreting it:

| Class | Examples |
| --- | --- |
| `CONTEXT` | product brief, business model, timeline, constraints |
| `QUANT` | event exports, funnels, cohorts, retention, adoption, revenue |
| `QUAL` | interview transcripts, notes, support tickets, sales calls |
| `USER_BELIEF` | author's thoughts, explanations, worries, ideas |
| `HYPOTHESIS` | explicit or reconstructed falsifiable claims |
| `GOAL` | objectives, targets, KPI/OKR definitions |
| `EXPERIMENT` | test specs, exposure data, A/B results |

Create a manifest. Record missing classes as gaps; do not pretend they exist.

## Phase gates

Follow `references/workflow.md`. At the end of each phase, write or maintain a
compact artifact:

- `00-manifest.md`
- `01-evidence-ledger.jsonl`
- `02-quant-findings.md`
- `03-qual-findings.md`
- `04-hypothesis-ledger.csv`
- `05-cross-synthesis.md`
- `06-goals-and-gaps.md`
- `07-final-report.md`

When file writes are unavailable, keep the same named sections in a compact
working ledger and do not repeat raw inputs.

Do not begin cross-synthesis until the independent quantitative and qualitative
passes are complete or explicitly marked unavailable.

## Upstream loading discipline

Use `references/router.md`.

- Load no upstream file merely because it exists.
- A normal phase loads one base method plus at most one specialist.
- The causal branch may load the three Clamp causal files.
- Experiment design/analysis may load the GrowthBook router plus one lifecycle
  reference, and optionally the platform-neutral Clamp result reader.
- Goal/OKR rules load only after findings are stable.
- Unload conceptually after producing the phase artifact; later phases consume
  the compact artifact, not the entire raw source and every upstream rule.

## Final deliverable

Follow `references/output-contract.md`. The report must explicitly answer:

- What is happening now?
- What evidence is trustworthy, weak, or missing?
- Which original hypotheses are supported, contradicted, mixed, untested, or
  superseded?
- What changed from the previous understanding?
- Where do quantitative behavior and interview narratives converge or conflict?
- Which segments behave differently?
- What are the most consequential gaps?
- Which goals remain valid, need sharpening, should be replaced, or are blocked
  by measurement?
- What new hypotheses and opportunities emerged?
- What should be measured, researched, tested, built, stopped, or decided next?

A conclusion without evidence IDs is incomplete. A long report without a clear
decision implication is also incomplete.
