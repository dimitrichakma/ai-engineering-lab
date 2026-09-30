# Explain my own code: worksheets

Five worksheets about code that Claude Code wrote in your real projects. The goal: after each one,
you can explain that file in an interview without looking.

## How to do a worksheet (about 1 hour)
1. **Without opening the file**, answer every question in your own words. Guessing is fine.
2. Open the real file and check each answer. Mark it ✅ right, 🟡 partly, ❌ wrong.
3. Fix the wrong ones, in your own words, with the line numbers that prove it.
4. Draw the flow on paper (boxes and arrows) and take a photo for your notes.
5. Finish with the "interview answer": 4 to 6 sentences you could say out loud.

**No AI for steps 1 to 4.** After that, you may ask Claude Code to check your answers (the lab's
`CLAUDE.md` tells it to point to lines, not give answers).

| # | Worksheet | Project | File |
| --- | --- | --- | --- |
| 1 | Guardrails | habit tracker | `src/agent.py` |
| 2 | Gateway | habit tracker | `src/main.py` |
| 3 | Tools and user scoping | habit tracker | `src/tools.py` |
| 4 | Corrective retrieval router | mental health chatbot | `src/router.py` |
| 5 | Safety screen | mental health chatbot | `src/safety.py` |
