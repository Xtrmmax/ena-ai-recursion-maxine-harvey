# Calendar Engine

## Overview
Built Mar–Jun 2025, with minor improvements through August 2025. This project encodes a mathematically complex calendar system with **10+ interdependent mechanisms** (cyclical offsets, modular resets, leap year adjustments, time-zone conversions, exception handling, etc.).  
Debugging required solving one layer at a time — unlike the Gregorian calendar, there’s no single linear formula.

## What’s Here
- `scripts/` → core Python code for calendar logic and dataset generation  
- `outputs/` → sample outputs and full dataset generator file (~3,000 entries)  
- `Initial_Output.md` → example system output (no input)  
- `User_Input_Output.md` → example output after user input  
- `Dataset_Generator.jsonl` → full 3,000-entry dataset (large file)  
- `Dataset_Generator_Sample.md` → readable subset (3 entries)  

## Results
- Produced consistent Mexica calendar outputs across thousands of test cases.  
- Successfully generated large datasets for downstream use (fine-tuning, prediction experiments).  

## Reflection
This project sharpened skills in **debugging, modular coding, datset creation and building deterministic systems**. Those skills directly strengthened later fine-tuning work.
