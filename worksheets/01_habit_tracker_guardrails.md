# Worksheet 1: Guardrails · habit tracker `src/agent.py`

Look at: `input_guardrail`, `output_guardrail`, `_INJECTION_PATTERNS`, `_LEAK_PATTERNS`,
`_CLASSIFIER_SYSTEM`, `OFF_TOPIC_BLOCK_CONFIDENCE`, `GUARDRAIL_TIMEOUT_SECONDS`, `build_agent`.

## Questions (answer first, check later)
1. In what order do the four middleware hooks run in `build_agent`? What does each one do?
2. `input_guardrail` returns early for some messages without checking them. Name two cases, and why each is safe to skip.
3. What happens when a regex in `_INJECTION_PATTERNS` matches? Is the LLM classifier still called?
4. What extra context does the classifier get besides the latest message? Why does that context exist? (Think of "the lesson isn't done yet".)
5. The classifier call times out. What does the user see, and why was that behaviour chosen?
6. When is an `OffTopic` message allowed through? What happens to it then?
7. Why do `PromptInjection` and `HarmfulBehavior` block at any confidence, but `OffTopic` doesn't?
8. What does the harmful refusal message point users to? Why doesn't it hard code a phone number?
9. `output_guardrail` has two kinds of checks. Which always runs, and which can be turned off with an env var?
10. Why does `_LEAK_PATTERNS` include every tool name from `TOOLS`?
11. `GuardrailClassification` uses `extra="forbid"`. What does that do, and why here?

## Draw it
One message from the user until the reply is shown, with every place it can be blocked or replaced.

## Interview answer
"How did you protect your agent against prompt injection?" (4 to 6 sentences)

## Compare with C2 of the lab
Two things your habit tracker does that your lab version doesn't, and one thing your lab version measures that the habit tracker doesn't.
