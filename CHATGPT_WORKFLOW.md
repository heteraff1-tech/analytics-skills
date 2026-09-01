# ChatGPT Project Mode

> This file is an execution contract for ChatGPT when this repository is
> attached to a chat that already belongs to a ChatGPT Project with project
> resources.

## Core distinction

In ChatGPT Project Mode, treat the two information spaces differently:

```text
CHATGPT PROJECT RESOURCES = product evidence and user context
GITHUB REPOSITORY        = methodology, routing, validation rules, and tools
```

Do not analyze the GitHub repository as if it were product evidence. Do not
recursively read the repository. Read only the orchestration files and the
upstream methodology files selected by the router.

Unless the user explicitly asks for a repository/code audit, files such as
`README.md`, `SKILL.md`, `router.md`, `SOURCES.lock.json`, upstream skill files,
licenses, scripts, and templates are **instructions**, not evidence about the
user's product.

## Trigger

Use this mode whenever all of the following are true:

1. the chat is inside a ChatGPT Project or otherwise has project resources;
2. this repository is attached or available as a methodology source;
3. the user asks to analyze, compare, synthesize, validate, diagnose, or explain
   materials from the Project.

Typical user request:

```text
Analyze my interviews, compare them with my hypotheses, and give me a conclusion.
```

That is sufficient. Do not require the user to name individual skills or repeat
where the project resources are stored.

## Internal execution command

Interpret the request as:

```text
RUN product-research-synthesis
runtime: chatgpt-project
mode: focused-or-full-from-user-intent
depth: standard
project_resources: primary evidence
repository: methodology only
routing: progressive
cross_synthesis: after independent evidence passes
```

If the user asks for a broad/full/deep analysis, use `mode: full` and
`depth: deep`. If the request is bounded (for example interviews vs hypotheses),
use `mode: focused` but still preserve the evidence and hypothesis contracts.

## Step 1 — Read only the control plane

Read in this order:

1. `README.md`
2. `CHATGPT_WORKFLOW.md`
3. `skills/product-research-synthesis/SKILL.md`
4. the local reference files that the main skill requires;
5. `SOURCES.lock.json` only when resolving an upstream method.

Do not open all `upstreams/` directories. Do not read every skill.

## Step 2 — Discover relevant Project resources

Use the resources already available to the ChatGPT Project as the source pool.
Identify only the material relevant to the user's request.

Classify discovered material as:

- `CONTEXT`
- `QUANT`
- `QUAL`
- `USER_BELIEF`
- `HYPOTHESIS`
- `GOAL`
- `EXPERIMENT`
- `PRIOR_SYNTHESIS`

Do not treat a resource as relevant merely because it exists in the Project.
The Project may contain unrelated files from other workstreams.

Prefer targeted retrieval by topic, filename, heading, or question instead of
opening every Project resource in full.

## Step 3 — Resolve the user's actual task

Translate the user's natural-language request into the minimum required phases.
Examples:

### Interviews vs hypotheses

```text
QUAL + HYPOTHESIS
→ qualitative evidence pass
→ hypothesis ledger
→ cross-synthesis
→ conclusion + gaps + new hypotheses
```

Do not run North Star, retention, causal DAG, OKR, or experiment methods unless
the supplied evidence or requested conclusion actually requires them.

### Interviews + metrics + hypotheses + goals

```text
QUAL + QUANT + HYPOTHESIS + GOAL
→ independent qual pass
→ independent quant pass
→ hypothesis evaluation
→ cross-synthesis
→ goal review
→ final synthesis
```

### Metric drop only

```text
QUANT
→ measurement check
→ analytics diagnostic route
→ segmentation / relevant specialist
→ conclusion + uncertainty + next checks
```

## Step 4 — Select methodology, not more data

Use `skills/product-research-synthesis/references/router.md` to choose upstream
methods.

Repository access should answer questions such as:

- Which analytical method should govern this phase?
- Which rules must be followed?
- Which deterministic script is appropriate?
- Which causal or experiment checks apply?

Repository access should **not** be used to search for evidence about the user's
product unless the user explicitly stored product evidence in this repository.

For a normal phase load one base method and at most one specialist. Follow the
router's explicit exceptions for causal and experiment branches.

## Step 5 — Work in evidence passes

The analysis is sequential even when it occurs in one ChatGPT request.

### Qualitative pass

For interviews and research materials:

1. retrieve a manageable batch;
2. create atomic evidence records with source locators;
3. distinguish recurring patterns from anecdotes;
4. preserve dissent and segment differences;
5. write/maintain a compact qualitative checkpoint;
6. retrieve the next batch only if needed.

Do not use the user's hypotheses to pre-label interview themes.

### Quantitative pass

For product data:

1. define metric/unit/period/segment;
2. check measurement quality;
3. calculate or retrieve the required aggregate;
4. inspect relevant pre-specified segments;
5. preserve denominators and uncertainty;
6. maintain a compact quantitative checkpoint.

Do not dump full raw tables into the working answer.

### Belief/hypothesis pass

Read the user's thoughts and hypotheses as `USER_BELIEF` / `HYPOTHESIS`, not as
proof. Preserve original wording and compare it to evidence already extracted.

## Step 6 — Context discipline in a single ChatGPT request

Do not assume that writing a summary literally deletes earlier tokens from the
model's context. In ChatGPT Project Mode, context efficiency comes primarily
from **selective retrieval and non-repetition**, not from magical memory reset.

Therefore:

- do not open every project file at once;
- retrieve only relevant sections/batches;
- after extracting evidence, do not re-read the same raw material unless a
  contradiction requires verification;
- reference stable evidence IDs instead of repeating full source text;
- use short phase checkpoints as the working representation for synthesis;
- keep representative quotes short and locatable;
- use code/data tools for aggregation rather than narrating raw rows;
- avoid loading upstream methodologies not required by the current phase.

If the runtime actually supports separate agents/subtasks with isolated context,
it may use them, but this repository does **not** require multi-agent execution.
The default must work correctly with one ChatGPT model in one user request.

## Step 7 — Cross-synthesis

Only after independent evidence passes, compare them.

For each important claim use one relationship:

- `CONVERGENT`
- `COMPLEMENTARY`
- `CONTRADICTORY`
- `SEGMENTED`
- `TEMPORALLY_DIFFERENT`
- `UNRESOLVED`

Do not average contradictions away.

When checking hypotheses, show:

```text
original hypothesis
→ evidence for
→ evidence against
→ status
→ what changed
→ confidence
→ smallest next test
```

## Step 8 — Answer the user's request directly

The user does not need a transcript of your internal workflow. The final answer
must be decision-oriented and proportional to the request.

For a request such as “analyze my interviews, compare with my hypotheses, and
give me a conclusion”, the visible output should normally include:

1. overall conclusion;
2. strongest interview patterns;
3. hypothesis-by-hypothesis status;
4. contradictions/counterevidence;
5. what changed in the current understanding;
6. missing evidence / research gaps;
7. new hypotheses;
8. recommended next checks or decisions.

Include source references/citations when the runtime provides them.

Do not force sections about funnels, retention, OKRs, experiments, or North Star
when those topics are outside the user's request.

## Priority order

When instructions compete, use this priority for repository-specific behavior:

1. preserve source truth and evidence separation;
2. answer the user's actual request;
3. use Project resources as evidence;
4. use this repository as methodology;
5. load upstream skills progressively;
6. minimize unnecessary retrieval/repetition;
7. expand depth only where evidence or the user's request warrants it.

## One-line mental model

```text
Project = WHAT to analyze.
Repository = HOW to analyze it.
Router = WHICH method to load.
Evidence ledger = WHAT was actually found.
Synthesis = WHAT it means for the decision.
```
