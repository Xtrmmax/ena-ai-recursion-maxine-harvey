# Calendar Engine

> Note: Before March 2025 I had never built a deterministic system with interlocking rules.  
> Using “vibe coding” — trial-and-error iteration with AI assistants — I built a calendar engine with at least 10 mathematical mechanisms (cyclical offsets, leap years, time zones, exception handling, etc.).  
> I still don’t know how to code, but I learned how to layer complex logic and debug one piece at a time until the whole system worked.


## Overview
From **March–June 2025**, I built a custom calendar engine as my second major technical project.  
Unlike the Gregorian calendar, this system required **at least 10 interdependent mathematical mechanisms** — such as cyclical offsets, modular resets, leap year adjustments, time-zone conversions, and exception handling for gap days.  

Each mechanism had to be coded, tested, and debugged in layers until the system worked end-to-end.  
This project gave me the confidence to tackle complex, deterministic systems and sharpened the coding/debugging skills I now apply back to fine-tuning.

## What’s Here
- `calendar_engine.py` → core Python code  
- `/datasets` → simplified JSON input files used by the engine  

## Results
- Completed a fully working calendar system with deterministic outputs.  
- Debugged across multiple interlocking layers (each piece depended on the last).  
- Extended the model in **Jul–Aug 2025** into a **Bitcoin price movement predictor** (manual Excel prototype for now).  

## Reflection
This was by far the most challenging part of my technical journey so far. The experience forced me to work in modules, integrate them carefully, and debug systematically. It shifted how I approach coding and gave me the foundation I now bring back into AI fine-tuning.  

## Next Steps
- Code the Bitcoin predictor (currently a manual Excel workflow).  
- Integrate calendar outputs into training datasets for future fine-tuned models.  
