# Calendar Engine ReadMe

For a quick overview, see the: [Calendar Executive Summary](./EXECUTIVE_SUMMARY.md)

> Note: Before March 2025 my only experience in Python was getting to Day 8 of 100 Days of Coding on Udemy.  
> Using “vibe coding” and trial-and-error iteration with AI assistants I built a calendar engine with at least 10 mathematical mechanisms (cyclical offsets, leap years, time zones, exception handling, etc.).  
> I still don’t know how to code, but I learned how to layer complex logic and debug one piece at a time until the whole system worked.

## Overview
From **March–June 2025**, I built a custom calendar engine as my second major technical project.  
Unlike the Gregorian calendar, this system required **10+ interdependent mechanisms** (cyclical offsets, modular resets, leap year adjustments, time-zone conversions, exception handling).  

Each piece had to be coded, tested, and debugged in layers until the system worked end-to-end.

## What’s Here
- `calendar_engine.py` → core Python code  
- `/datasets` → simplified JSON input files used by the engine  
- `/outputs` → generated calendar outputs and dataset generator results  

## Results
- Completed a working calendar system with deterministic outputs.  
- Debugged across multiple interlocking layers (each mechanism depended on the last).  
- Extended the system in **Jul–Aug 2025** into a **Bitcoin price movement predictor** (manual Excel prototype for now).  

## Reflection
This project pushed me to think modularly, integrate carefully, and debug systematically.  
It became the foundation for how I now approach fine-tuning and more advanced AI experiments.

## Next Steps
- Code the Bitcoin predictor (currently manual in Excel).  
- Integrate calendar outputs into training datasets for future fine-tuned models.  


## Transition to ENA.ai Recursion

The Calendar Engine was my first experiment with deterministic behavioral modeling — a system that used the **Mexica (Aztec) calendar** to generate dynamic personality and trait forecasts from cyclical symbolic inputs such as glyphs, directions, and day rulers.  
Each combination produced a unique behavioral signature, effectively acting as a **predictive personality generator** rather than a static calendar.

This project introduced the idea that **patterns of time can reveal patterns of self**.  
That same principle became the foundation for **ENA.ai Recursion**, which replaced symbolic time with emotional geometry.  
Where the calendar predicted behavioral expression through cosmic cycles, the **TemporalNeedEngine (TNE)** now predicts emotional regulation through affective cycles — using valence, arousal, and trust as its temporal coordinates.

Both systems share the same core architecture:
> deterministic input → cyclical transformation → interpretable, symbolic output.

In other words, ENA.ai Recursion is the emotional successor to the calendar engine —  
a system that transforms rhythm into regulation, and pattern into process.

> Note: Only one dataset (`simplified_day_glyphs.json`) is shown for illustration.  
> The full symbolic model includes multiple archetypal mappings (direction, ruler, nahual, solar wave, etc.),  
> stored privately to protect intellectual property.