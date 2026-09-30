# Worksheet 5: Safety screen · mental health chatbot `src/safety.py` (+ `crisis_resources.py`)

Look at: `MessageCheck`, `screen_message`, `CRISIS_KEYWORDS`, `_keyword_hit`, `_resolve_country`,
`build_crisis_response`, `DOMAIN_REFUSAL`.

## Questions
1. What two things does one classifier call decide? Why combine them into one call?
2. What are the three risk levels, and what does each one mean?
3. "Crisis always wins." What does that mean in code?
4. When are `CRISIS_KEYWORDS` used? Why not always?
5. Give one message where keywords get it wrong in each direction (false alarm and miss). The docstring has examples.
6. If the classifier fails, are off topic messages blocked? Why was that choice made?
7. Why does the classifier see the last 3 turns of history? What goes wrong without it?
8. When is the user's IP looked up, and why only then?
9. The country can't be found. What does the crisis response show?
10. For Somajji you decided to change this design. List the 3 changes and why each one matters for volunteers in the Chittagong Hill Tracts.

## Draw it
One message from arrival to one of the three outcomes: crisis, off topic, or continue.

## Interview answer
"How did your mental health chatbot handle users in crisis?"

## Compare with Worksheet 1
The habit tracker blocks on classifier failure; the chatbot falls back to keywords. Which is safer for a mental health app, and why?
