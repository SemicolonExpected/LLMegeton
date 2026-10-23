# Agentic AI

## What is AI and GenAI compared to other things

Some think AI and ML are two distinct groups of algorithms when in reality, it’s comparing apples to oranges. Machine learning is a type of AI. AI algorithms aren’t necessarily machine learning based, nor are they stochastic (uses statistics). The “intelligence” part just means decision making. An *artificial intelligence algorithm* is just _an algorithm where a machine makes decisions_—even simple ones. Pathing algorithms for video games are AI. [Here’s a video on how A*](https://youtu.be/i0x5fj4PqP4?is=hU8tmcgtkwDewM7m), a pathfinding algorithm from the 1960’s works. Classifiers like spam filters are AI.

Of course, colloquially now, when we use the term AI, we think of “Generative AI”(GenAI)—
People consider “GenAI” distinct from “Assistive AI” and ML. Assistive AI is not a technical term.
All of what we call GenAI is deep learning based, a subset of machine learning. *Generative AI* is just _an algorithm that generates new content using AI_ and has been around since the 90s. Procedural generation like Minecraft or No Man Sky maps are GenAI. Alexa and Text to Speech is Generative AI. 
GenAI is used to generate accurate data to train classifiers when you don’t have enough data and you can’t reasonably gather that data ethically. Deepfake detection is type of classifier that uses Generative Adversarial Networks in a cat and mouse type game where the generative side tries to fool the detector and the detector gets better at not getting fooled.

Whether the AI is “assistive” or not is based on the tool and subjective. Unless you mean like a personal assistant, which is agentic, a because you have “agents” who use generative models to orchestrate a task. A chat consists of a single agent at a time.
This one you give it a task via prompt, it interprets the prompt and tries to do it. 
Today’s agentic bots are usually multi-agent where the main bot decides whether its capable or feasible doing the task itself or needs to delegate the tasks to more specialized agents. Depending on the architecture it could look like simple parallel computing and the sub agents are just copies of the main one so each one could do anything the others can, or structured like a little business with different departments where different roles are assigned at the time of creation.
Claude Code is this second type. Each project has a main “coordinator” Claude who just makes “thread” Claudes to delegate tasks to. These thread Claudes can make “helper” Claudes to do various tasks. 
My copy of Claude Code system prompt states it should not “spawn agents unless the user asks” because they “start cold and re-derives context you [thread Claude] already have” which is akin to training a new employee. It costs a lot of tokens to rewrite the instructions for this assistant, so these aren’t tokenomicly viable unless needed for something tedious and you don’t want to lock up that thread Claude.

In both of these cases, the goal is to coordinate tasks so well, it looks like there’s only one agent.
Architecturally, it’s like a small talking ant colony or bee hive with talking bees

## Major Labs

| Lab | Major Model Lines | Open or closed | Country |
|---|---|---|---|
| Anthropic | Claude | Closed | US |
| Meta | Muse Spark, Muse Wonder | Mixed: Spark has an open weights version | US |
| Google | Gemini | Closed | US |
| OpenAI | ChatGPT | | US| 
| DeepSeek | V4-Pro, V4.1 Flash | Open (MIT) | China |
| Alibaba (Qwen) | Qwen3.8-Max | Mixed: smaller models open, the multimodal flagship API-only | China |
| Zhipu (GLM) | GLM-5.3 | Open (custom license; Flash is MIT) | China |
| Moonshot (Kimi) | Kimi K3 | Open (own license) | China |
| MiniMax | M3 | Open | China |
| Tencent | Hy4 Preview | Open (Apache 2.0) | China |
| Baidu | Ernie 5.1 | Closed | China |
| ByteDance | Doubao Seed 2.1 Pro | Closed | China |
