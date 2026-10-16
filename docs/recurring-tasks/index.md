# Recurring Tasks

The evocations: reusable prompt patterns for directing language models. Each pattern is a tool — reach for the right one for the job.

## Role framing

Tell the model *who to be* before telling it *what to do*.

```
You are a senior database engineer reviewing a migration plan.
```

**When to use it:** when the task benefits from a specific expertise lens or tone. It narrows the model's vast possibility space toward the register you want.
**Watch out:** roles don't grant real expertise — "you are a lawyer" doesn't make the output legal advice. It's a style and framing aid, not a capability unlock.

## Few-shot examples

Show, don't just tell. Give 2–4 input/output pairs demonstrating exactly what you want.

```
Classify the sentiment of each review as positive, negative, or mixed.

Review: "Arrived fast, works great." → positive
Review: "Broke after a week, terrible." → negative
Review: "Good product, awful packaging." → mixed
Review: "..." →
```

**When to use it:** format-sensitive tasks, classifications, style imitation. Often more effective than paragraphs of instruction.
**Watch out:** examples bias the model — unrepresentative examples produce unrepresentative outputs. Choose them deliberately.

## Chain-of-thought

Ask the model to reason step by step before answering.

```
Solve this step by step, showing your work, then give the final answer.
```

**When to use it:** math, logic, debugging, any multi-step problem. The intermediate steps both improve accuracy and make errors auditable.
**Watch out:** longer chains cost more tokens and the model can still go confidently wrong mid-chain. Verify, don't trust.

## Structured output

Demand a specific format: JSON, tables, headings, bullet constraints.

```
Respond with valid JSON only, matching this schema: {...}
```

**When to use it:** when another system (or a picky human) consumes the output. Eliminates the "great answer, wrong shape" problem.
**Watch out:** specify the schema completely — models fill gaps with confident invention.

## Constraints and negatives

Say what *not* to do, and bound the task.

```
Keep it under 150 words. No jargon. Don't mention the competitor.
```

**When to use it:** almost always, as a complement to other patterns. Constraints are cheap and disproportionately effective.
**Watch out:** over-constraining can strangle useful output. Leave room for the thing you actually want.

## Iterative refinement

Don't aim for perfect in one shot — generate, critique, revise.

```
Draft it. Then critique your draft against these criteria: [...]. Then revise.
```

**When to use it:** writing, design, anything with quality criteria you can name. The model critiquing its own output is surprisingly effective.
**Watch out:** without concrete criteria the "critique" step just flatters the draft.
