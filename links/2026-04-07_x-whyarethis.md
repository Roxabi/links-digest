---
title: "As promised.  Our first paper and contribution to the amazing work going on t..."
source: "https://x.com/whyarethis/status/2041609904524595504?s=12"
date: 2026-04-07
tags: ["Machine Learning", "Transformers", "Model Optimization", "Physics", "Open Source"]
platform: x
author: "@whyarethis"
summary: "Researchers introduced a universal physics-derived formula that identifies dead attention heads in transformers to automate model pruning without losing quality."
---
As promised.  Our first paper and contribution to the amazing work going on to make open source models smaller, faster, and more accessible.

So what is it, and why is it important? 

We discovered what appears to be a universal formula that identifies dead attention heads in any transformer, derived from physics — not fitted from data.

This is wild, because up till now finding and pruning dead heads has been a manual job of trial and error.  By removing unused heads, the models can get smaller and faster while still maintaining competitive quality.

The core insight is geometric. LayerNorm projects every token's hidden state onto a high-dimensional sphere. Once you see that, attention heads become couplings between oscillators on that sphere — the same mathematical object physicists have studied for 50 years. And in oscillator physics, there's a precise critical point (the BKT phase transition) below which a coupling is dead. It contributes nothing. 

We transferred that critical point into transformer geometry and got a single formula: tau = 0.96 / sqrt(d). No parameters to tune. No model-specific calibration. You plug in the hidden dimension and it tells you which heads are dead. We validated it across six models in four architecture families — GPT-2, Qwen, Llama, Gemma — at 95-100% precision.

What excites us most isn't the formula itself. It's that this same geometric understanding — treating transformers as coupled oscillator networks — has informed everything we've built since. 

We have a full coherence-guided compression pipeline (structured pruning, channel optimization, role-aware quantization) coming soon that uses the same single forward pass to understand a model's entire anatomy. This paper is the foundation. The repo includes a standalone scanner you can run on any Hugging Face model right now.

Hopefully this work and this formula will be useful to other researchers to lead to more deterministic optimization pipelines.

#project89

https://github.com/project-89/coherence-guided-dead-head-identification