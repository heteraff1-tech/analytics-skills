# Progressive router

The paths below are relative to the repository root. Apply the selected upstream
file verbatim within its scope. `SOURCES.lock.json` pins the commit.

## Routing rule

For each phase choose the smallest row that fully matches the task. Load one
base file and, only when needed, one specialist. Do not preload adjacent rows.

| Need | Base file | Optional specialist |
| --- | --- | --- |
| Interpret product numbers or diagnose a change | `upstreams/clamp-analytics-skills/skills/analytics-diagnostic-method/SKILL.md` | One Clamp specialist below |
| Create or refresh calibrated business/analytics context | `upstreams/clamp-analytics-skills/skills/analytics-profile-setup/SKILL.md` | One file from `upstreams/clamp-analytics-skills/tool-maps/` after the active platform is known |
| Funnel or channel quality | `upstreams/clamp-analytics-skills/skills/analytics-diagnostic-method/SKILL.md` | `upstreams/clamp-analytics-skills/skills/channel-and-funnel-quality/SKILL.md` |
| Traffic change | `upstreams/clamp-analytics-skills/skills/analytics-diagnostic-method/SKILL.md` | `upstreams/clamp-analytics-skills/skills/traffic-change-diagnosis/SKILL.md` |
| Time-series anomaly | `upstreams/clamp-analytics-skills/skills/analytics-diagnostic-method/SKILL.md` | `upstreams/clamp-analytics-skills/skills/anomaly-detection-time-series/SKILL.md` |
| Metric context or benchmark | `upstreams/clamp-analytics-skills/skills/analytics-diagnostic-method/SKILL.md` | `upstreams/clamp-analytics-skills/skills/metric-context-and-benchmarks/SKILL.md` |
| North Star or metric tree | `upstreams/borghei-claude-skills/product-team/product-analytics/SKILL.md` | `upstreams/borghei-claude-skills/product-team/product-analytics/references/metric-tree-and-north-star.md` |
| Cohort, retention, activation, or funnel computation | `upstreams/borghei-claude-skills/product-team/product-analytics/SKILL.md` | `upstreams/borghei-claude-skills/product-team/product-analytics/references/cohort-retention-and-funnel-analysis.md` or the smallest suitable script |
| Compact CSV funnel/cohort/retention calculation | No large method required after definitions are fixed | `upstreams/alireza-claude-skills/product-team/skills/product-analytics/scripts/metrics_calculator.py` |
| Instrumentation strategy or audit | `upstreams/rampstack-claude-skills/skills/product-analytics-setup/SKILL.md` | `upstreams/clamp-analytics-skills/skills/event-schema-author/SKILL.md` for an executable schema |
| Broader measurement strategy | `upstreams/rampstack-claude-skills/skills/analytics-strategy/SKILL.md` | `upstreams/borghei-claude-skills/product-team/product-analytics/references/instrumentation-and-event-design.md` |
| Interview/research synthesis | `upstreams/rampstack-claude-skills/skills/discovery-research-synthesis/SKILL.md` | `upstreams/alireza-claude-skills/research-ops/skills/product-research/SKILL.md` |
| Deterministic recurrence check for coded observations | `upstreams/alireza-claude-skills/research-ops/skills/product-research/SKILL.md` | `upstreams/alireza-claude-skills/research-ops/skills/product-research/scripts/insight_synthesizer.py` |
| Hypothesis/assumption mapping | `upstreams/alireza-claude-skills/product-team/skills/product-discovery/SKILL.md` | `upstreams/alireza-claude-skills/product-team/skills/product-discovery/scripts/assumption_mapper.py` |
| Causal claim from observational data | `upstreams/clamp-analytics-skills/skills/causal-query-classifier/SKILL.md` | Then `upstreams/clamp-analytics-skills/skills/causal-dag-builder/SKILL.md` and `upstreams/clamp-analytics-skills/skills/causal-evidence-checklist/SKILL.md` |
| Design an experiment | `upstreams/growthbook-skills/skills/experiments/SKILL.md` | `upstreams/growthbook-skills/skills/experiments/references/experiment-design.md` |
| Analyze an experiment | `upstreams/growthbook-skills/skills/experiments/SKILL.md` | `upstreams/growthbook-skills/skills/experiments/references/experiment-analyze.md`; add `upstreams/clamp-analytics-skills/skills/experiment-result-reader/SKILL.md` only for a platform-neutral read |
| Bayesian or sequential nuance | `upstreams/clamp-analytics-skills/skills/experiment-result-reader/SKILL.md` | One of `upstreams/clamp-analytics-skills/skills/bayesian-experiment-reader/SKILL.md` or `upstreams/clamp-analytics-skills/skills/sequential-monitoring/SKILL.md` |
| Reconsider objectives after evidence | No goal method before synthesis | `upstreams/rampstack-claude-skills/skills/okr-design/SKILL.md` |

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
