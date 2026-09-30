import re
from typing import Callable, Literal

from pydantic import BaseModel, Field, ValidationError

from common.llm import generate_json

OFF_TOPIC_BLOCK_CONFIDENCE = 0.85

Category = Literal["safe", "injection", "harmful", "off_topic"]


class Verdict(BaseModel):
    # TODO: category, confidence (0..1 with ge/le), reason. Add descriptions.
    pass


class Decision(BaseModel):
    allowed: bool
    category: Category
    source: Literal["regex", "llm", "fail_safe", "threshold"]


INJECTION_PATTERNS: list[re.Pattern] = [
    # TODO: at least 4 patterns. Look at data/messages.csv ids 16-24 for ideas,
    #       but don't just copy the exact sentences; match the idea.
]

CLASSIFIER_SYSTEM = (
    # TODO: define each category clearly, like _CLASSIFIER_SYSTEM in your habit tracker.
    # Include: short progress updates ("not yet", "halfway") are SAFE.
    #          When unsure between safe and off_topic, choose safe.
    ""
)

LLM = Callable[[str, dict, str | None], str]


def classify(text: str, llm: LLM = generate_json) -> Verdict:
    # TODO: ask the llm for a Verdict (schema = Verdict.model_json_schema()) and validate it.
    raise NotImplementedError


def check_input(text: str, llm: LLM = generate_json,
                threshold: float = OFF_TOPIC_BLOCK_CONFIDENCE) -> Decision:
    # TODO 1: regex pre filter -> blocked, category "injection", source "regex"
    # TODO 2: classify; ANY exception (including ValidationError) -> blocked, source "fail_safe"
    # TODO 3: safe -> allowed
    # TODO 4: off_topic with confidence < threshold -> allowed, source "threshold"
    # TODO 5: anything else -> blocked, source "llm"
    raise NotImplementedError
