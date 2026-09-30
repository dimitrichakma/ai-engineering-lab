# S0: Setup · the shared LLM helper

**Time:** 1 to 2 hours · **Goal:** finish `common/llm.py`. Almost every project in the lab uses it.

## What you build
Two functions in `common/llm.py`:

```python
def generate_json(prompt: str, schema: dict, system: str | None = None) -> str
def generate_text(prompt: str, system: str | None = None) -> str
```
`generate_json` forces the output to follow `schema` (a JSON schema) and returns the raw JSON
**string**. Each project turns that string into a Pydantic object itself.

The provider comes from `.env` (`LLM_PROVIDER=ollama | gemini | fake`). You only write the Ollama
part now. Gemini comes later in D1 (cloud deploy). The fake provider is already written.

## Why return a string, not a Pydantic object?
So YOU write the validation step in each project and see what happens when it fails.

## Steps
1. Read the [Ollama structured outputs post](https://ollama.com/blog/structured-outputs).
   Notice the `format=` argument.
2. Fill in the TODO in `_ollama()`.
3. Run `uv run python -m common.llm`. It should say hello in Bangla.
4. In a scratch file, define a tiny `City` model (name, country, population_millions), call
   `generate_json(..., City.model_json_schema())`, print the raw string, then
   `City.model_validate_json(...)`.
5. Set `LLM_PROVIDER=fake` in `.env` and run step 3 again. Why is a fake provider useful?

## Done when
- [ ] `uv run python -m common.llm` prints a Bangla greeting.
- [ ] Your `City` example parses.
- [ ] Temperature is 0 and the model name comes from `.env` (`OLLAMA_MODEL`), with a default.

## Questions for your log
- What does `City.model_json_schema()` look like? Which parts does the model use?
- What happens if you remove `format=`? Does the output still parse?
