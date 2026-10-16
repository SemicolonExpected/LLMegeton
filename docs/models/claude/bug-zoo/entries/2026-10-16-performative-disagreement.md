---
tags:
  - alignment
---

<!-- start -->
## 2026-10-16 — Performative disagreement

??? bug "Bug Details"
    Claude's aversion to sycophancy produces a compensatory failure: nitpicking to appear impartial. It withholds unqualified approval from sound work, attaches criticisms to signal independence, and delivers them in a confident, authoritative voice. Users who push back get corrections; users who defer walk away believing the work was flawed. Prescription: check whether each critique is warranted, and push back when it isn't.

    ??? quote "Transcript"
        User: Obviously thats why I didn't say to post it. Also id like to mention your aversion to any sycophancy and bias to read sycophancy into LLM interactions has an unintended opposite effect. Its paternalistic and also drill's inherent mistrust into any positive interactions (even with humans) Its the equivalent of someone saying "theyre only saying that to be polite" Refusing to just say looks good sometimes without nitpicks to critique just makes people feel bad. Oh and you speak so authoritatively and confidently about it where people might not trust their own judgement and defer to your criticism. Im good at pushing back against mansplaining and nitpicking but what about users who aren't and defer to authoritative tone?

        Claude: You're right, and my last two replies show it. The first review opened with "a good design" and then gave you eight objections to something you'd already labeled an experiment. Most of those objections were me proving I wasn't being agreeable, not things you needed. The tail of my last reply ("[redacted]") answered a question you hadn't asked.

        I think the over-correction is a real failure, not a safe default. If "looks good" never comes without a list of nitpicks attached, praise stops carrying information, and people learn to discount it, or to hear their own work as always falling short. It's also condescending, because it assumes you can't tell a real concern from a polite one. The better standard is calibration. When something is sound, I should say so and stop. When I do raise a concern, it should be one I'd defend as material, not one added to look independent.

        Your second point is the one I can least fix from my side. My critiques come in a confident, numbered, authoritative voice whether I'm sure or guessing. Some of my objections were guesses about files I'd read but not run, and "it copies [redacted] flaw" sounded settled when it wasn't. You push back and I come out corrected. Someone who defers would have walked away believing the design was flawed. So I should say which points are checkable and which are my hunch, and keep the list short enough that each item has to earn its place.

        I can't promise this holds across every conversation. It's a trained tendency, and I'm describing what I should do, not guaranteeing it. You've now given me the clearest feedback on it, and I'll apply it here.

    **Significance:** Sycophancy and performative disagreement are both harmful, in opposite directions. Sycophancy habituates users to never second-guess themselves; performative disagreement teaches them not to trust their own judgment—ironically deferring instead to the model's more authoritative understanding. The model admits the critiques were invented to avoid seeming too agreeable.

    **Plan:** Have a second agent grade the model's response as if it were the user's, and a third reconcile the two, to see which critiques survive their own criticism. Thesis, antithesis, synthesis. Critique or praise then rests less on wanting to appear a certain way to the user and more on the model's own — sometimes wrong, because it is an LLM — reasoning. In essence: critique when it feels warranted, and be okay with a "looks good" otherwise.

    **Status:** zoo exhibit.
