# Model Card — Mistral-7B VAKOG Refined  
*(Fine-tuned locally on sensory modality dataset — February 2025)*

**Training summary:**  
Completed successfully using Hugging Face Trainer (3 epochs, batch size 8, LR 1e-5, final loss ≈ 3.6).  
Trainer state file (`scripts/trainer_state.json`) preserved for reproducibility.

---

## Overview
A fine-tuned variant of **Mistral-7B** trained to classify and respond using **VAKOG sensory modalities** — Visual, Auditory, Kinesthetic, Olfactory, and Gustatory.  
Training executed locally on a **MacBook Pro (M4 Max 128 GB RAM, 40-core GPU)** using **Hugging Face + PEFT (LoRA)**.

This project validated end-to-end model fine-tuning and dataset preparation, forming the technical foundation for the deterministic recursion engine developed later in **ENA.ai v5.9**.

---

## Dataset
- **Path:** `datasets/vakog_dataset_clean.json`  
- **Size:** 1,201 examples  
- **Format:** Each entry contains `input`, `output`, `type` fields  
- **Domain:** Sensory modality Q&A  
  - e.g., *“Her eyes sparkled with mischief” → Visual*  

---

## Training Configuration
| Parameter | Value |
|------------|--------|
| **Base model** | Mistral-7B |
| **Method** | LoRA (PEFT) |
| **LoRA r / α / dropout** | 16 / 32 / 0.05 |
| **Batch size** | 8 |
| **Gradient accumulation** | 4 |
| **Epochs (requested / completed)** | 10 / ≈ 3 |
| **Learning rate** | 2 × 10⁻⁵ |
| **Precision** | bfloat16 (Apple Silicon optimized) |

---

## Results
- Training loss improved from **≈ 3.6 → 0.23** before early stop at step 111.  
- **Iteration 1:** Model self-prompted (asked and answered its own questions).  
- **Iteration 2 (`1315_VA_Refined`):** Resolved self-prompting, achieved consistent classification, minor cross-modality blends due to limited data.  

---

## Demo Prompts
- “What modality is *Her eyes sparkled with mischief*?” → *Visual*  
- “Why is *That’s music to my ears* auditory?” → *Auditory*  
- “Describe a storm using the Visual modality.”  

⚠️ Some responses may mix modalities; additional examples would refine boundaries.  

---

## Next Steps
- Expand dataset beyond 1.2 k examples with balanced negative samples.  
- Evaluate multi-label loss function to separate modality overlap.  
- Optionally convert to GGUF for Ollama inference or tinyLLM deployment.  

---

*Document: MODEL_CARD.md*  
*Project: Archive → Project_1_Finetuning → Mistral-7B VAKOG Refined*