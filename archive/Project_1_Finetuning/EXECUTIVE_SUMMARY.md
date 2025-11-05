# Fine-Tuning Work — Executive Summary

> Before February 2025, I had never fine-tuned a model or configured an AI development environment.  
> Through rapid iteration and AI-assisted experimentation, I learned to prepare datasets, manage dependencies, and fine-tune large models within two weeks.

## Overview
Within **14 days of starting**, I successfully fine-tuned a variant of **Mistral-7B** on a **1,200-example VAKOG sensory-modality dataset**.  
This project was my first hands-on technical build and the foundation for all later ENA.ai recursion work.

## Contents
- `scripts/finetune_vakog.py` — Training script (Hugging Face Trainer).  
- `datasets/vakog_dataset_clean.json` — 1,201 curated sensory examples.  
- `scripts/trainer_state.json` — Training metadata (3 epochs, LR 1e-5, loss ≈ 3.6).  
- `MODEL_CARD.md` — Training parameters, evaluation notes, and results.

## Results
- **First run:** model began self-prompting (resolved through dataset cleanup).  
- **Second run:** achieved consistent modality classification; occasional cross-modality overlap due to dataset size.  
- Validated full fine-tuning pipeline from data prep → model training → output verification.

## Demo
Example evaluation prompts:
- “What modality is *Her eyes sparkled with mischief*?” → *Visual*  
- “Why is *That’s music to my ears* auditory?” → *Auditory*  
- “Describe a storm using the Visual modality.”

## Reflection
By June 2025, I paused fine-tuning to design the deterministic **calendar engine**, which evolved into the **ENA.ai Recursion** architecture.  
That transition marked my shift from model tweaking to **emotion as geometry — regulation as math.**
