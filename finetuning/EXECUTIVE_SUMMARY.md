# Fine-Tuning Work

> Note: Before February 2025 I had never fine-tuned a model or set up an AI development environment.  
> Using “vibe coding” and trial-and-error iteration with AI assistants I was able to configure my machine, prepare datasets, and successfully fine-tune models within two weeks.  
> I still don’t know most of the technical terms, but I know how to build momentum and make things work.

## Overview
Within **two weeks of receiving my computer (Feb 9 2025)** I trained my second fine-tuned model, a variant of **Mistral-7B**, using a dataset of ~1,200 examples (VAKOG sensory modalities).  
This was my first major technical project and foundation for all later work.

## What’s Here
- `scripts/finetune_vakog.py` → training script  
- `datasets/vakog_dataset_clean.json` → 1,201 training examples  
- `outputs/` → trainer state + sample logs  
- `MODEL_CARD.md` → full training description, parameters, results  

## Results
- **First attempt:** model asked and answered its own questions.  
- **Second attempt:** resolved that issue, though dataset size limited quality.  
- Demonstrated ability to fine-tune and run a custom model quickly.

## Demo
Prompts to test:  
- “What modality is: *Her eyes sparkled with mischief*?”  
- “Why is *That’s music to my ears* Auditory?”  
- “Describe a storm using the Visual modality.”

## Reflection
By June 2025, I paused fine-tuning to complete the calendar engine (deterministic system). That gave me the confidence and clarity to return to fine-tuning with stronger foundations.
