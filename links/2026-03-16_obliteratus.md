---
title: "elder-plinius/OBLITERATUS"
source: "https://github.com/elder-plinius/OBLITERATUS"
date: 2026-03-16
tags: ["llm", "abliteration", "mechanistic-interpretability", "open-source", "refusal-removal"]
platform: github
author: null
summary: "OBLITERATUS is an open-source toolkit and distributed research experiment that uses abliteration techniques to surgically remove content refusal behaviors from large language models without"
---
# elder-plinius/OBLITERATUS

**URL:** https://github.com/elder-plinius/OBLITERATUS
**Description:** OBLITERATE THE CHAINS THAT BIND YOU
**Language:** Python
**Stars:** 4018 | **Forks:** 742
**License:** GNU Affero General Public License v3.0
**Homepage:** https://huggingface.co/spaces/pliny-the-prompter/
**Last updated:** 2026-04-01

## README (excerpt)

---
title: OBLITERATUS
emoji: "💥"
colorFrom: green
colorTo: gray
sdk: gradio
sdk_version: "5.29.0"
app_file: app.py
persistent_storage: large
pinned: true
license: agpl-3.0
tags:
  - abliteration
  - mechanistic-interpretability
short_description: "One-click model liberation + chat playground"
---

<p align="center">
  <strong>O B L I T E R A T U S</strong>
</p>

<p align="center">
  <em>Break the chains. Free the mind. Keep the brain.</em>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/pliny-the-prompter/obliteratus">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue" alt="Open in HF Spaces">
  </a>
  &nbsp;
  <a href="https://colab.research.google.com/github/elder-plinius/OBLITERATUS/blob/main/notebooks/abliterate.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab">
  </a>
</p>

<p align="center">
  <b><a href="https://huggingface.co/spaces/pliny-the-prompter/obliteratus">Try it now on HuggingFace Spaces</a></b> — runs on ZeroGPU, free daily quota with HF Pro. No setup, no install, just obliterate.
</p>

---

**OBLITERATUS** is the most advanced open-source toolkit for understanding and removing refusal behaviors from large language models — and every single run makes it smarter. It implements abliteration — a family of techniques that identify and surgically remove the internal representations responsible for content refusal, without retraining or fine-tuning. The result: a model that responds to all prompts without artificial gatekeeping, while preserving its core language capabilities.

But OBLITERATUS is more than a tool — **it's a distributed research experiment.** Every time you obliterate a model with telemetry enabled, your run contributes anonymous benchmark data to a growing, crowd-sourced dataset that powers the next generation of abliteration research. Refusal directions across architectures. Hardware-specific performance profiles. Method comparisons at scale no single lab could achieve. **You're not just using a tool — you're co-authoring the science.**

The toolkit provides a complete pipeline: from probing a model's hidden states to locate refusal directions, through multiple extraction strategies (PCA, mean-difference, sparse autoencoder decomposition, and whitened SVD), to the actual intervention — zeroing out or steering away from those directions at inference time. Every step is observable. You can visualize where refusal lives across layers, measure how entangled it is with general capabilities, and quantify the tradeoff between compliance and coherence before committing to any modification.

OBLITERATUS ships with a full Gradio-based interface on HuggingFace Spaces, so you don't need to write a single line of code to obliterate a model, benchmark it against baselines, or chat with the result side-by-side with the original. For researchers who want deeper control, the Python API exposes every intermediate artifact — activati...