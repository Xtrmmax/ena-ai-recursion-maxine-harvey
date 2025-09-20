For a quick overview, see the [Executive Summary](EXECUTIVE_SUMMARY.md).

> Note: Before 2025 I had never fine-tuned a model or built anything in Python beyond completing Day 8 in 100 Days to Code on Udemy.  
> Using “vibe coding” and trial-and-error iteration with AI assistants I set up my machine, fine-tuned Mistral-7B within two weeks, and later built a calendar engine with at least 10 interlocking mathematical mechanisms.  
> I still don’t know most of the technical terms, but I know how to build momentum, debug one layer at a time, and make complex systems work.


# YC_Application_Silaiclone_Maxine_Harvey_Portfolio

**YC Portfolio: Mistral-7B fine-tuning + custom calendar engine**

Hands-on technical work demonstrating:

- Fine-tuning a large language model (Mistral-7B with LoRA)  
- Building a mathematically complex calendar system
- Building a dataset generator

> **Notice:** This repository is proprietary and provided exclusively for YC application review.  
> You may view and run the code for evaluation purposes only.  
> Do not copy, modify, or redistribute without written permission.  

---

## Project Roadmap
- `/finetuning` → AI model fine-tuning work, training scripts, dataset, and results  
- `/calendar` → Calendar engine with Python code and mathematical documentation  

---

## Fine-Tuning Work

Within **two weeks of receiving my new computer (Feb 9–25, 2025)** I prepared a dataset, ran fine-tuning, and produced a working variant of **Mistral-7B** trained on **VAKOG sensory modalities**.

### What’s Here
- `finetune_vakog.py` → training script  
- `datasets/vakog_dataset_clean.json` → 1,201 training examples  
- `MODEL_CARD.md` → detailed description of training run, results, and demo prompts  

### Results
- **First model:** produced odd behavior (asking and answering its own questions).  
- **Second iteration (`1315_VA_Refined`):** fixed that issue but still blended modalities, showing the need for a larger dataset.  

Even so, this demonstrates rapid progress — moving from zero setup to a fine-tuned large language model in under three weeks.  

---

## Calendar Engine

From March–June 2025 I shifted focus to build a **calendar system** with interlocking mathematical rules.  
The system encodes **at least 10 different mathematical mechanisms** (cyclical offsets, modular resets, leap year adjustments, time-zone conversions, exception handling for gap days, etc.).  

Each module had to be built, tested, and integrated before the system worked end-to-end. Unlike the Gregorian calendar, there’s no single linear formula — every piece is interdependent, so debugging required solving it one layer at a time.  

Within the calendar is embedded a dataset generator currently set to 3000 outputs, but scalable beyond that. 

This gave me deeper skills in **vibe coding, debugging, dataset creation and designing complex deterministic systems**, which I will now bring back to the fine-tuning track.  
