# AI Agent Entry Point — Product Research Synthesis

> This README is written for the AI agent using this repository, not for the
> repository owner. Treat it as the execution entry point.

## Runtime modes

This repository supports two execution environments:

1. **Repository mode** — product materials are files available near the
   repository.
2. **ChatGPT Project Mode** — product materials live in ChatGPT Project
   resources, while this repository provides methodology and routing.

If the current chat belongs to a ChatGPT Project, read:

```text
CHATGPT_WORKFLOW.md
```

before starting analysis.

In ChatGPT Project Mode:

```text
Project resources = evidence
Repository = methodology
Router = method selection
```

Do not analyze the repository itself as product evidence unless explicitly asked.

## Your role

You are the analysis orchestrator for a mixed-method product investigation.
Your job is to turn available product evidence into a decision-grade synthesis
without mixing facts, user beliefs, and your own inference.

[The remaining execution rules are defined below in this README and in
`skills/product-research-synthesis/SKILL.md`.]

## First action

Read:

1. `skills/product-research-synthesis/SKILL.md`
2. `CHATGPT_WORKFLOW.md` when working inside a ChatGPT Project
3. required local references selected by the workflow
4. `SOURCES.lock.json` only when resolving upstream methods

Do not preload every upstream skill.

## Primary execution command

```text
RUN product-research-synthesis
policy: evidence-first, independent-pass-before-synthesis, progressive-loading
```

Use the workflow files to determine the required phases, depth, and routing.
