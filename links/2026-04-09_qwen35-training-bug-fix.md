# Qwen3.5-35B-A3B Training Bug Fix — FernflowerAI GGUF

**Source:** https://www.reddit.com/r/LocalLLaMA/comments/1sfwauj/qwen3535ba3buncensoredfernfloweraigguf/
**Date:** 2026-04-09
**Tags:** Qwen3.5, local LLM, bug fix, MoE, GGUF

---

**The find:** u/EvilEnginer spent two weeks digging into the Qwen3.5-35B-A3B weights and identified a training bug in Alibaba's **original release** — not the GGUF or the uncensored finetune.

**Root cause chain:**
- AdamW optimizer + MoE (256 experts) + DeltaNet recurrent layers → rare experts in late blocks get disproportionately high effective learning rate → weight drift
- Affected: `ssm_conv1d.weight` tensors in **blocks 36 & 37**
- Scale was ~60% too high (σ=0.102 vs median 0.063)
- DeltaNet hidden state corrupts → model loses context mid-conversation

**Symptoms (now explained):**
- "Philosophizing" / rambling on long conversations
- Context loss after ~50–70k tokens
- Looping, indecision, broken code generation
- No amount of parameter tuning fixes it — it's in the weights

**The fix:** Scale those two tensors back to normal. 489 other tensors untouched. Result: **88.6% error reduction** on 35B, **90.7%** on 27B.

**Also confirmed broken:** Qwen3.5-27B (8 broken tensors), Unsloth BF16 quant, official Alibaba release. Gemma 4 26B A4B checked — clean.

---

**Relevance to your setup:** You're running an RTX 3080 (prod) — the fixed Q4_K_L quant runs on a 3060 12GB at ~10 tok/s in LM Studio, so it should be comfortable on your 3080. Worth trying if you've been using Qwen3.5 35B A3B for any long-context tasks on Lyra or voiceCLI.

**Downloads:**
- [35B GGUF (fixed)](https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-GGUF)
- [35B safetensors](https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-safetensors)
- [27B GGUF (experimental)](https://huggingface.co/LuffyTheFox/Qwen3.5-27B-Claude-4.6-Opus-FernflowerAI-GGUF)
