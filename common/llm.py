"""Shared LLM helper for the whole lab. You write it once in S0 (Track 1) and reuse it everywhere.

generate_json(prompt, schema, system) -> str   JSON text that should follow `schema` (not validated)
generate_text(prompt, system) -> str            plain text reply

The provider comes from .env, so the SAME code runs on your laptop and in the cloud (see D1):
    LLM_PROVIDER=ollama   local, free (default)
    LLM_PROVIDER=gemini   free tier API key WITHOUT a billing account (used in D1 cloud deploy)
    LLM_PROVIDER=fake     canned answers, for demos and tests when no model is available
"""
import os
import json
from dotenv import load_dotenv
import ollama

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")


def _messages(prompt: str, system: str | None) -> list[dict]:
    msgs = [{"role": "system", "content": system}] if system else []
    msgs.append({"role": "user", "content": prompt})
    return msgs


def _ollama(prompt: str, system: str | None, schema: dict | None) -> str:
    # TODO (S0): ollama.chat(model=OLLAMA_MODEL, messages=_messages(prompt, system),
    #            format=schema (only if not None), options={"temperature": 0})
    #            return the message content
    response = ollama.chat(model=OLLAMA_MODEL,messages=_messages(prompt, system),format=schema,options={"temperature": 0})
    return response.message.content


def _gemini(prompt: str, system: str | None, schema: dict | None) -> str:
    # TODO (D1, optional earlier): read the CURRENT Gemini structured output docs
    #   https://ai.google.dev/gemini-api/docs/structured-output
    # Use GEMINI_API_KEY from .env. Never commit the key.
    raise NotImplementedError


def _fake(prompt: str, system: str | None, schema: dict | None) -> str:
    # Given. Returns something valid-looking so an app can run with no model at all.
    if schema is None:
        return "This is a fake reply (LLM_PROVIDER=fake)."
    return json.dumps({"note": "fake output; fields may not match the schema"})


_PROVIDERS = {"ollama": _ollama, "gemini": _gemini, "fake": _fake}


def generate_json(prompt: str, schema: dict, system: str | None = None) -> str:
    return _PROVIDERS[PROVIDER](prompt, system, schema)


def generate_text(prompt: str, system: str | None = None) -> str:
    return _PROVIDERS[PROVIDER](prompt, system, None)


if __name__ == "__main__":
    print(generate_text("Say hello in Bangla, in one short sentence."))
