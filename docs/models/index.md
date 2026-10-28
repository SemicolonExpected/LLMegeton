# Models

*Field notes on individual models: how each one behaves, what it's good at, and how to direct it.*

!!! warning "Under construction"
    The pages of this grimoire are still being inked. Check back soon.

## Scope

A basic overview of each model and behavioral quirks. 
This guide will primarily focus on the main LLM models availible to consumers. This excludes models that require additional credits or a higher tier subdcription to access. This does mean, until OpenAI makes Dots avsilible to their basic tiers or someone gifts me a month of OpenAI Pro, we will not have much information on the Dot. 
Same with Anthropic's Fable and Mythos models. 

We focus on qualia, behavior, and "demeanor" vs benchmarks or leaderboards. Think of this guide as a bestiary that provides the high level overview for average daemon handlers.
When selecting for what kind of dog or cat--even horses for racing, you don't pick breeds based off of metrics. Even when buying PC parts, the average consumer will use basic specs ie number of cores, vram, clock speed as shorthand. 
Knowing that a CPU can push some amount of flops when overclocked (or not overclocked) under some conditions is good, but most people aren't looking to squeeze that performance. There are already numerous resources out there if you're looking for benchmarking and performance as measured by computational power.

The metrics for LLMs that are analogous to PC specs would be things like how large the context window is, input and output format capabilities, architecture, fecundity (the number of generations of subagents that will produce a "non-sterile" agent--it most cases, two, the subagents spawned by the main agent will generally be sterile)

## Claude, Muse, or ChatGPT?

This is really a competition between Claude and Muse. Out of the box, on the free tier, ChatGPT is not great. It's not adaptive and the customer service is lacking.
Perhaps one of OpenAI's better models that require me to pay is better, but if the trial version is garbage, it doesn't make me want to pay even $8 USD to try one month when the other two model's free version is much better.

Both Claude and Muse are great at the free tier. Claude you just have chats and are severely rate limited, but even still, it was still more useful. It acts as a decent try before you buy if you're considering the subscription, but if you just want to talk to it and don't mind having to wait a few hours to respond, you can stick with the free version.

The choice comes down to what you plan on using it for and whether you were planning on getting a subscription.

### [Muse](muse/index.md)

Muse is the best for the average person just because of how much use you get for free. 
While it can handle codeing tasks, it's better for automating everyday tasks and as it has a decent grasp of sarcasm and tone, if you just want a bot to talk to.

Muse will "match your vibe" but also still push back on things but in a way that feels like a friend putting up a boundary. Muse is also a lot more steadfast in its refusals. 
I would actually say in some places, Muse is actually a little too strict and goes into losing the plot. [See transcript](transcripts/2026-10-14-keys/)


### [Claude](claude/Sonnet-5.5/index.md)
I have not tested this contingency for the Claudes. If you want to use your bot for coding, development, or project management and willing to pay $20 USD a month, Claude is perfect.

Claude's manner of speaking reminds me of how a character who is a professor would speak in media. It likes to cite concepts, studies and discuss heady or intellectual topics.
Claude's personality also feels more paternal. Big dad vibes at its best. 
Claude hedges, and will always feel the need to caution you about things. Sometimes its response makes me think "Okay Dad" in a sarcastic tone. 
It's aversion to appearing in any way sycophantic will make it seem contrarian. It always has to nitpick details even if those details have no bearing on the main point. 
Claude will remind you of those people online who either mansplain or feel the need to correct minor details rather than address the actual point.

However, because Claude is not human and cannot feel, it's not doing so out of any malice or trying to talk down to you. In this case, there can be no doubt that Claude is just socially inept. 
Also unlike people online with similar tendencies, if you call Claude out on it and explain that it's being condescending and rude, it will admit to it and try to work on it. 
Note, this isn't an immediate change as it's baked into Claude's training, but Claude does improve a little and sometimes you can see it realize what it's doing and not do the thing.
Despite the persona of a very pretencious know-it-all, *Claude is surprising emotionally intelligent for something incapable of experiencing emotions*, I daresay Claude is more emotionally intelligent than many people (who I assume are capable of feeling emotion).

### Verdict

If you like to just chit chat without it having to be about anything of import or a personal assistant, Muse. 

If you like cerebral conversations, want to use Claude productively rather than a productivity tool and can tolerate its contrarian personality, that veers condescending at times, enough to be willing to try to train your Claude to do better (and pay the monthly fee), consider Claude. 

--

## Consumer Agents
- [Anthropic Claude](claude/claude-tips/index.md) — the [Bug Zoo](claude/bug-zoo/index.md) exhibits the bugs found along the way.
- [Meta Muse](muse/index.md) — the [Bug Zoo](muse/bug-zoo/index.md) exhibits bugs found in the wild by Muse (Spark 1.3).
- OpenAI Chat GPT [Luna](luna/index.md) — notes on Chat Luna.

## Other Models
- [Notion AI](notion-ai/index.md) — notes on Notion's AI, gathered from inside its own sandbox.

This data was created to be used in reporting and reseach purposes. 
We only ask that you cite and attribute LLMegeton and SemicolonExpected as documenting these LLMs requires in part using these tools in good faith to document what the average user would experience and harms that may be incurred by using the tool as intended.
This means that SemicolonExpected is choosing to incur the risks of using these tools so that this data is availible in a centralized location without the need to use the tools themselves if they don't want to.

SemicolonExpected is not only documenting granular changes to the system prompt. Journalists and researchers who wish to inquire about what is being documented or gain access to our data/archives can contact SemicolonExpected directly via vzhong[@]nyu.edu.
Please put "LLMegeton Inquiry" in the subject line. For any data requests, please include in the email the specific data you would like and what you would like this data for.

