---
title: "Dead Head Identification in Transformers"
source: "https://x.com/whyarethis/status/2041609904524595504"
date: 2026-04-07
tags: []
platform: x
author: @whyarethis
---

# Dead Head Identification in Transformers

**Source:** https://x.com/whyarethis/status/2041609904524595504
**Date:** 2026-04-07
**Author:** @whyarethis

---

--|
| **Formula** | `τ = 0.96 / √d` — where `d` = hidden dimension |
| **Input** | Hidden dimension only |
| **Output** | Which attention heads are dead (contribute nothing) |
| **No tuning** | Zero model-specific calibration |
| **Validated on** | GPT-2, Qwen, Llama, Gemma — 95–100% precision |

## The Physics Angle

- LayerNorm → projects token hidden states onto a **high-dimensional sphere**
- Attention heads → become **couplings between oscillators** on that sphere
- Physics analogy: **BKT phase transition** — below the critical point, a coupling is dead and contributes nothing

## Why It Matters

- Dead head pruning was previously **manual trial-and-error**
- This makes it **deterministic and universal** — plug in `d`, get dead heads
- Smaller + faster models with **no quality degradation**

## Repo

[github.com/project-89/coherence-guided-dead-head-identification](https://github.com/project-89/coherence-guided-dead-head-identification)