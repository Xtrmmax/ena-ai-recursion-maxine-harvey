# Model Card: Mistral-7B VAKOG Refined (2025-02-25)

**Model Path (local):**  
Trained weights are stored locally (not included in this repo due to size).

---

## Overview
This model is a fine-tuned variant of **Mistral-7B** trained to classify and respond using **VAKOG sensory modalities** (Visual, Auditory, Kinesthetic, Olfactory, Gustatory).  
Training was performed locally on a MacBook Pro (M4 Max, 128 GB RAM, 40-core GPU).  

The model was fine-tuned with **Hugging Face + PEFT (LoRA)**.

---

## Dataset
- **Source file:** `datasets/vakog_dataset_clean.json`  
- **Size:** 1,201 examples  
- **Format:** Each entry contains `input`, `output`, and `type` fields  
- **Domain:** Sensory modality Q&A (e.g., *“Her eyes sparkled with mischief” → Visual*)  

---

## Training Details
- **Base model:** Mistral-7B  
- **Fine-tuning method:** LoRA  
  - r = 16  
  - α = 32  
  - dropout = 0.05  
- **Batch size:** 8  
- **Gradient accumulation:** 4  
- **Epochs requested:** 10  
- **Epochs completed:** ~3 (early stop at step 111)  
- **Learning rate:** 2e-5  
- **Precision:** bfloat16 (optimized for Apple Silicon)  

---

## Results
- Loss reduced from **~3.6 → ~0.23** over training  
- Early runs showed:
  - First model: asked and answered its own questions  
  - Second iteration (`1315_VA_Refined`): fixed self-answering bug, but still needed more data for polished responses  

---

## Demo
Try asking:  
- “What modality is: *Her eyes sparkled with mischief*?”  
- “Why is *That’s music to my ears* auditory?”  
- “Describe a storm using the Visual modality.”  

⚠️ Responses may blend modalities (needs further data expansion).  

---

## Next Steps
- Increase dataset size beyond 1,201 examples  
- Add modality-specific negative samples to reduce mixing  
- Optional: convert to GGUF format for smooth chat in Ollama  
