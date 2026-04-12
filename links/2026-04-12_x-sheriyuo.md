---
title: "Agentic RL: Decoupling Reasoning from Tool-Use"
source: "https://x.com/sheriyuo/status/2042895889132363815?s=12"
date: 2026-04-12
tags: []
platform: x
author: "@sheriyuo"
summary: ""
---
With the rise of Agentic RL, LLMs are no longer just one-shot Q&A systems. They are evolving into agents that repeatedly interact between reasoning and external tool use in multi-turn trajectories. From Search-R1 to ToolRL and SkyRL, a clear technical direction is emerging: models must learn not only how to think, but also how to search, calculate, and call APIs, improving themselves through RL over long trajectories.

Yet most of these methods rest on an implicit assumption: reasoning ability and tool-use ability can be jointly optimized within the same shared parameter space, and this joint training should create synergy.

The paper Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning challenges that assumption with systematic evidence. The authors show that in Agentic RL, reasoning and tool use are often not synergistic at all. Instead, they can strongly interfere with each other. In other words, when a model learns “how to reason” and “how to use tools” in the same parameters, improving one often comes at the expense of the other.

This is not a quirk of a single task or a small model. The phenomenon appears consistently across different datasets and model scales. The root cause is not mainly data or reward design, but optimization dynamics. By analyzing token-level gradients, the authors find that gradient directions from reasoning tokens and tool-call tokens are close to orthogonal, with angles near 90 degrees.

That means the two capabilities are searching for very different optima in parameter space. When they are forced to update the same parameters, training can only move toward a compromise direction, which is suboptimal for both sides. This creates a structural gradient conflict that limits the upper bound of Agentic RL performance.

Q1: Why do we observe near-orthogonal gradients?

From a linear algebra perspective, in high-dimensional space, two random vectors g_1 and g_2 are very likely to be nearly orthogonal. More precisely, if the dimension is large, the angle between two randomly sampled vectors concentrates around 90 degrees. That is a basic fact of high-dimensional geometry.

\frac{\mathbf{g}_1^\top \mathbf{g}_2}{\|\mathbf{g}_1\|\|\mathbf{g}_2\|} \approx 0

In Agentic RL, reasoning tokens and tool-use tokens come from different data distributions and different objectives, so the gradients they induce in parameter space are close to “random vectors” with respect to each other. Geometrically, near-orthogonality is therefore not surprising. It is the norm in high-dimensional spaces.

Suppose the reasoning gradient is g_r​ and the tool gradient is g_t​. Under joint training, the actual update is g_r + g_t. If the two are orthogonal, then the update is not optimal for either side. For reasoning, g_t​ behaves like noise. For tool use, g_r​ also behaves like noise.

Q2: If this is true, why does pretraining not suffer from such severe conflict?

Because pretraining and post-training live in very different geometric regimes. In pretraining, the objective is language modeling, so different tasks such as translation, QA, math, and code still share a common core structure. Their gradients are often aligned around improvements in low-level linguistic representations, such as lexical, syntactic, and semantic features.

In Agentic RL post-training, however, the reasoning objective is to build better internal chains of thought, while the tool-use objective is to generate API calls and control-flow decisions. Their optimal representational structures are very different: one is centered on internal reasoning trajectories, the other on external action selection. The gradients therefore come from semantically different control objectives, making orthogonality and conflict much more likely.

To move beyond intuition, the authors introduce LEAS (Linear Effect Attribution System), a diagnostic framework for quantifying synergy and interference between abilities. The key idea is to decompose model capability into binary variables, introduce interaction terms to capture the effect of joint training, and then construct multiple model variants to solve a linear system. This reveals the sign and magnitude of each interaction coefficient. A negative coefficient means the two abilities interfere with each other under joint optimization.

The results show that on multi-tool QA tasks such as NQ and HotpotQA, the interaction term between reasoning and tool use is negative for almost all examples. This directly challenges the assumption that shared parameters naturally create synergy.

Even more interestingly, the strongest interference appears exactly in the hardest cases, where multi-step reasoning and tool interaction are truly required. This suggests that Agentic RL hits its biggest bottleneck in the very scenarios where it should matter most.

After establishing that interference is real and widespread, the authors propose a direct solution: instead of forcing conflicting abilities to compete inside the same shared parameters, decouple them at the parameter level. This method is called DART (Disentangled Action-Reasoning Tuning).

The basic idea is simple. Freeze the original backbone parameters, then attach two separate LoRA adapters: one for reasoning and one for tool use. A token-level routing mechanism decides which subspace receives the gradient for each token. Reasoning tokens update only the reasoning LoRA, and tool tokens update only the tool LoRA. This creates explicit gradient isolation during training.

This is very different from traditional multi-task learning approaches that try to reduce conflict through loss weighting or gradient projection. DART does not attempt to find a compromise in shared space. Instead, it accepts that different abilities need different parameter subspaces and lets them evolve independently in their own low-rank spaces.

In forward propagation, the model still looks like a normal backbone with a routed LoRA branch added on top. But in optimization, reasoning and action are already fully separated.

The experiments show that this disentanglement strategy leads to stable and significant gains on multiple tool-augmented QA benchmarks. At the 3B scale, DART improves average EM by more than 6% over Search-R1-GRPO, and on multi-hop reasoning tasks the relative gain is close to 30%. More importantly, when the retrieval results are fixed, DART still clearly outperforms the jointly trained model. This means the improvement does not come from better retrieval. It comes from reasoning itself no longer being dragged down by joint optimization.

The authors also compare DART with a 2-Agent system, where one separate model handles reasoning and another handles tool decision-making. In theory, this avoids gradient conflict and serves as a performance upper bound. The result is striking: DART reproduces most of the performance advantage of the 2-Agent setup within a single-model architecture, while avoiding the heavy engineering cost of multi-model systems, including memory usage, context switching, and KV-cache rebuilding.

That matters a lot for real deployment. It means capability disentanglement does not have to come at the cost of inference efficiency.

Q3: Why does DART work? A linear algebra view

At its core, DART assigns different abilities to different parameter subspaces.

W \to W + B_r A_r \quad (\text{reasoning}), \quad W + B_a A_a \quad (\text{action})

It effectively constructs two approximately orthogonal low-rank subspaces

\mathbf{g}_r \in \mathcal{S}_r,\quad \mathbf{g}_a \in \mathcal{S}_a,\quad \mathcal{S}_r \cap \mathcal{S}_a \approx \varnothing

so that the gradients for reasoning and tool use no longer interfere in the same parameter region. Each capability can converge independently in its own space.

That is why DART can approach the performance ceiling of a 2-Agent system while staying inside a single model.

More broadly, the significance of this work goes beyond one specific method. It reveals a principle that has been overlooked in agent system design: not all capabilities should be jointly trained in a shared parameter space. When different abilities exhibit systematic conflict in gradient geometry, parameter disentanglement can be more direct and effective than complex reward shaping or gradient surgery.

DART also gives LoRA a new role. It is no longer just a parameter-efficient fine-tuning tool. It becomes a carrier for capability modularization and structural disentanglement.

Overall, this work adds a new lens for thinking about Agentic RL: the performance bottleneck may not come from model size or reward design, but from structural conflict between abilities. By explicitly disentangling reasoning and action in parameter space, the model can preserve the independent optimality of both within a single architecture.

That idea is not only useful for tool-augmented QA. It may also point to a broader training paradigm for future large models with multiple capabilities.

For a clearer comparison between DART and Mixture-of-Experts (MoE), the related work section of the paper provides a detailed discussion, which is worth checking out if you are interested.

Open-source reproduction: https://github.com/sheriyuo/DART