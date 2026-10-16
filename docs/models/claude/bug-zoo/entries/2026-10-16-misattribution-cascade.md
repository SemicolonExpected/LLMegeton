---
tags:
  - thought crime
---

<!-- start -->
## 2026-10-16 — misattribution cascade

??? bug "Bug Details"
    Side effect of the [sticky flag, blind retry](2026-10-16-sticky-flag-blind-retry.md). The safeguard notice attaches to messages by position, each following a user reply, without identifying which content triggered it. Both user and model are left inferring trigger-from-position — and the inference is unreliable.

    Per the model's own reconstruction: after the initial stop (video 1's text, not video 2's as first assumed), the notice appeared attached to four later messages. Inferred trigger replies, by position: (1) the reply offering t1.txt and t3.txt after stating no finished transcript existed, notice attached to "Send me the text"; (2) the reply declining a line-by-line pass, notice attached to the binary-search message; (3) the reply declining the binary search, notice attached to "send me the clean one." The model's own words: "I'm inferring which reply each notice refers to from its position, since the notice itself doesn't say. I don't know what in those replies triggered it, and they were all plain prose."

    The cascade: unable to distinguish a new flag from a leftover one, the model attributes the flag to its most recent safe action and grows hesitant — declining the binary search, declining the line-by-line pass. Meanwhile the notices did not stop t3.txt from being delivered: the flag's bark is decoupled from its bite, which makes the misattribution worse, not better. Nothing in the episode tells the model what was actually wrong.

    **Assessment:** Positional flagging without causal attribution trains superstitious behavior. The model learns to fear its last action rather than the actual trigger, and refusals spread to safe work. This is the sticky flag's second-order effect: the first bug corrupts the retry loop, this one corrupts the model's self-model.

    **Plan:** Notices should name the triggering turn and content, not just attach to a position in the thread. A flag that cannot say what it flagged cannot be learned from — by the user or the model.

    **Status:** zoo exhibit.
