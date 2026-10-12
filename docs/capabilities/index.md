# Capabilities

What language models can actually do — and where they fall over. This is the honest map, not the marketing copy.

!!! note "A note on dates"
    Model capabilities move fast. Anything here dated more than ~6 months ago deserves a second look.

## Language

The home turf: generating, summarizing, translating, rewriting, and answering questions in natural language. Fluency is essentially solved; factuality is not. A model can write a beautiful paragraph that is completely wrong, with total confidence.

**Strong at:** drafting, brainstorming, tone-shifting, summarization, translation between natural languages.
**Weak at:** knowing when it's wrong. Calibration (matching confidence to correctness) remains poor — treat all factual claims as unverified until checked.

## Reasoning

Models can work through multi-step problems — math, logic puzzles, debugging — especially when asked to show their work step by step. But "reasoning" here means *producing the surface form of reasoning*, which usually (not always) tracks actual reasoning.

**Strong at:** problems that decompose cleanly, debugging with full context, working through structured arguments.
**Weak at:** long chains without verification, novel problems far from training distribution, knowing when a plausible-sounding step is actually invalid.

## Code

One of the most reliable capabilities: writing, explaining, and debugging code across most mainstream languages. Code has a built-in verifier (it runs or it doesn't), which makes this far more trustworthy than prose generation.

**Strong at:** boilerplate, common patterns, explaining unfamiliar code, translating between languages, test generation.
**Weak at:** large novel architectures, subtle correctness (race conditions, security), keeping a whole codebase coherent over long sessions.

## Tool use

Modern models can call functions, use APIs, browse, run code, and operate software through defined interfaces. This is what turns a chatbot into an agent: the model decides *when* to act and *which* tool to use.

**Strong at:** well-defined tools with clear schemas, multi-step tasks with verifiable intermediate states.
**Weak at:** ambiguous tool choice, recovering from tool errors gracefully, knowing when *not* to act.

## Vision and multimodality

Most frontier models now accept images (and some, audio/video) as input. They can describe, compare, extract text (OCR), and reason about visual content.

**Strong at:** describing images, reading screenshots and documents, comparing visual variants.
**Weak at:** precise spatial reasoning, counting many small objects, fine-grained visual detail, anything requiring pixel-level precision.

## Memory and context

Context windows have grown enormously, but "fits in context" ≠ "reliably used." Models attend unevenly — strong at the start and end, weaker in the middle ("lost in the middle").

**Strong at:** holding a decent working set of facts for a single session.
**Weak at:** true long-term memory across sessions (needs external scaffolding), reliably using everything in a very long context.

## The meta-capability

The most underrated LLM capability: **being directed well**. A model's output quality is largely a function of input quality — which is why the [Prompts](../prompts/index.md) and [Skills](../skills/index.md) sections exist. The grimoire's whole thesis: the spirits are willing; the evocations need work.
