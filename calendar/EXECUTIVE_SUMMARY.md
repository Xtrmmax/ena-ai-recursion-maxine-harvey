# Calendar Engine

## Executive Summary
For a high-level description of this project, see the [Calendar Executive Summary](../calendar/EXECUTIVE_SUMMARY.md).

> Note: Before March 2025 my only experience in Python was getting to Day 8 of 100 Days of Coding on Udemy.  
> Using “vibe coding” and trial-and-error iteration with AI assistants I built a calendar engine with at least 10 mathematical mechanisms (cyclical offsets, leap years, time zones, exception handling, etc.).  
> I still don’t know how to code, but I learned how to layer complex logic and debug one piece at a time until the whole system worked.

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
This project sharpened skills in **debugging, modular coding, dataset creation and building deterministic systems**. Those skills will directly strengthen upcoming fine-tuning work.
