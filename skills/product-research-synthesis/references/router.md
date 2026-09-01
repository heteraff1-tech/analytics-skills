# Progressive router

The paths below are relative to the repository root. Apply the selected upstream
file verbatim within its scope. `SOURCES.lock.json` pins the commit.

## Routing rule

For each phase choose the smallest row that fully matches the task. Load one
base file and, only when needed, one specialist. Do not preload adjacent rows.

| Need | Base file | Optional specialist |
| --- | --- | --- |
| Interpret product numbers or diagnose a change | `upstreams/clamp-analytics-skills/skills/analytics-diagnostic-method/SKILL.md` | One Clamp specialist below |
| Funnel or channel quality | base diagnostic method | `upstreams/clamp-analytics-skills/skills/channel-and-funnel-quality/SKILL.md` |
| Traffic change | base diagnostic method | `upstreams/clamp-analytics-skills/skills/traffic-change-diagnosis/SKILL.md` |
| Time-series anomaly | base diagnostic method | `upstreams/clamp-analytics-skills/skills/anomaly-detection-time-series/SKILL.md` |
| Metric context or benchmark | base diagnostic method | `upstreams/clamp-analytics-skills/skills/metric-context-and-benchmarks/SKILL.md` |
| North Star or metric tree | `upstreams/borghei-claude-skills/product-team/product-analytics/SKILL.md` | `.../references/metric-tree-and-north-star.md` |
| Cohort, retention, activation, or funnel computation | `upstreams/borghei-claude-skills/product-team/product-analytics/SKILL.md` | `.../references/cohort-retention-and-funnel-analysis.md` or the smallest suitable script |
| Compact CSV funnel/cohort/retention calculation | no large method required after definitions are fixed | `upstreams/alireza-claude-skills/product-team/skills/product-analytics/scripts/metrics_calculator.py` |
| Instrumentation strategy or audit | `upstreams/rampstack-claude-skills/skills/product-analytics-setup/SKILL.md` | Clamp `event-schema-author/SKILL.md` for an executable schema |
| Broader measurement strategy | `upstreams/rampstack-claude-skills/skills/analytics-strategy/SKILL.md` | Borghei `instrumentation-and-event-design.md` |
| Interview/research synthesis | `upstreams/rampstack-claude-skills/skills/discovery-research-synthesis/SKILL.md` | Alireza `research-ops/skills/product-research/SKILL.md` |
| Deterministic recurrence check for coded observations | Alireza product-research method | `.../scripts/insight_synthesizer.py` |
| Hypothesis/assumption mapping | `upstreams/alireza-claude-skills/product-team/skills/product-discovery/SKILL.md` | `.../scripts/assumption_mapper.py` |
| Causal claim from observational data | Clamp `causal-query-classifier/SKILL.md` | Then `causal-dag-builder/SKILL.md` and `causal-evidence-checklist/SKILL.md` |
| Design an experiment | `upstreams/growthbook-skills/skills/experiments/SKILL.md` | `.../references/experiment-design.md` |
| Analyze an experiment | GrowthBook experiment router | `.../references/experiment-analyze.md`; add Clamp `experiment-result-reader/SKILL.md` only for a platform-neutral read |
| Bayesian or sequential nuance | Clamp `experiment-result-reader/SKILL.md` | One of `bayesian-experiment-reader/SKILL.md` or `sequential-monitoring/SKILL.md` |
| Reconsider objectives after evidence | no goal method before synthesis | `upstreams/rampstack-claude-skills/skills/okr-design/SKILL.md` |

## Selection precedence

1. Use the file that matches the current artifact and decision.
2. Prefer deterministic scripts for arithmetic once definitions are settled.
3. Use qualitative methods only on qualitative artifacts; do not let them
   interpret product metrics.
4. Use quantitative methods only after data-quality checks.
5. Use the causal branch only for causal language or action based on
   observational evidence.
6. Use experiment rules only when an experiment exists or is being designed.
7. Use OKR rules only after the evidence and hypothesis ledgers are stable.

## Conflict handling

Upstream files remain independent authorities inside their scopes. If two
selected files conflict:

- quote or precisely identify both rules;
- explain which scope each rule targets;
- choose the more specific rule for the current artifact;
- record the unresolved methodological conflict if specificity does not resolve
  it;
- never rewrite both into an invented hybrid.
