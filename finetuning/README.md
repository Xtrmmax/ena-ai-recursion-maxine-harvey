# Fine-Tuning Work

📄 For a quick overview, see the [Fine-Tuning Executive Summary](./EXECUTIVE_SUMMARY.md).


> Note: Before February 2025 I had never fine-tuned a model or set up an AI development environment.  
> Using “vibe coding” and trial-and-error iteration with AI assistants I was able to configure my machine, prepare datasets, and successfully fine-tune models within two weeks.  
> I still don’t know most of the technical terms, but I know how to build momentum and make things work.

## Overview
Within two weeks of receiving my new computer on **Feb 9, 2025**. By **Feb 25, 2025**, I had trained my **second fine-tuned Mistral-7B model** on ~1,200 examples (`vakog_dataset_clean.json`).  
This was my first major technical project. I then pivoted to the calendar project (Mar–Jun 2025) to practice coding on a deterministic system. In **Jul–Aug 2025**, I extended the calendar model to build a **Bitcoin price movement predictor**. That gave me the confidence and clarity to return to fine-tuning with a stronger foundation.

## Results
- **First attempt:** Model asked/answered its own questions (buggy).  
- **Second attempt (Feb 25):** Fixed that issue, but dataset size limited response quality.  
- Proved I could fine-tune and run a custom model quickly, even if refinement is still needed.  

## Demo
This model runs and reflects training on **sensory modalities (VAKOG: Visual, Auditory, Kinesthetic, Olfactory, Gustatory)**.  
Responses are not yet refined and the model tends to **mix modalities together** rather than isolate one clearly.  
Even so, the outputs show the effect of fine-tuning compared to a base model.  

Try asking:  
- *“What modality is: ‘Her eyes sparkled with mischief’?”*  
- *“Why is ‘That’s music to my ears’ Auditory?”*  
- *“Describe a storm using the Visual modality.”*  

## Reflection
- **Feb 9, 2025:** Computer arrived  
- **Feb 25, 2025:** Second fine-tuned model trained successfully (~1,200 examples)  
- **Mar–Jun 2025:** Built and completed the calendar project (complex deterministic system)  
- **Jul–Aug 2025:** Extended calendar project into a **Bitcoin price movement predictor**  
- **Sep 2025 onward:** Returning to fine-tuning with clearer roadmap and stronger coding foundation  

## Next Steps
- Expand dataset from ~1,200 to 5K+ strong examples to reduce mixing of modalities  
- Add evaluation prompts to test for modality isolation more consistently  
- Apply structured approach from the calendar and Bitcoin predictor projects to improve fine-tuning discipline  
