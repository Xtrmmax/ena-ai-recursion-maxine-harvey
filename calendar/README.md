# Calendar Project

## Overview
From **Mar–Jun 2025**, I built and completed a working calendar engine in Python.  
Unlike the Gregorian calendar, this system required multiple interlocking cycles and exceptions, which made it much more complex. I had to build each part separately, test it, and then stitch them together so they functioned as one system. This was the most technically challenging project I’ve completed.

The calendar system encodes at least **10 different mathematical mechanisms** (cyclical offsets, modular resets, leap year adjustments, time zone conversions, exception handling for gap days, etc.). Each module had to be built, tested, and integrated before the system worked end-to-end. Unlike the Gregorian calendar, there’s no single linear formula — every piece is interdependent, so debugging required solving it one layer at a time.

## What I Did
- Encoded repeating cycles of years, days, and glyphs using modular arithmetic  
- Implemented offsets and lookup tables for groups of 20-day sequences  
- Added leap year corrections to keep the math aligned  
- Built special handling for “gap days” that break the cycle and restart it  
- Used precise hour/minute boundaries to determine exact year transitions  
- Integrated time zone normalization and DST error handling  
- Mapped final dates to multiple layers of traits

## Results
- Calendar engine produces accurate results across centuries  
- Proved I could solve a complex, non-linear mathematical system end-to-end  
- Gave me the confidence to return to fine-tuning with stronger vibe coding skills  

## Extension: Bitcoin Price Predictor
- In **Jul–Aug 2025**, I extended this system into a **manual Excel version** that compared calendar cycles Bitcoin price history  
- This was not coded in Python, but served as a practical proof of how the model could integrate with real-world datasets  

## Reflection
- **Mar–Jun 2025:** Completed the calendar project (first fully working system coded on my own)  
- **Jul–Aug 2025:** Applied it manually to Bitcoin investing as a predictor  
- Next: code the Bitcoin predictor and unify it with my fine-tuning work  

