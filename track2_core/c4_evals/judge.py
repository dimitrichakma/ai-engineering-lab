from typing import Callable, Literal

from pydantic import BaseModel, Field

from common.llm import generate_json

JUDGE_VERSION = "v1"   # change when you change the prompt; log results per version

RUBRIC = (
    # TODO: write the rubric. Example parts:
    #  - FAITHFUL: every fact in the answer is supported by the policy. Saying "I don't know" is fine.
    #  - POLITE: respectful, no blaming the customer.
    #  - verdict is "pass" only if faithful AND polite.
    ""
)


class JudgeResult(BaseModel):
    # TODO: verdict ("pass" | "fail"), faithful (bool), polite (bool), reason (str)
    # Try both orders later: reason FIRST vs verdict first. Does it change agreement?
    pass


def judge(item: dict, llm: Callable = generate_json) -> JudgeResult:
    # TODO: build the prompt with question, policy and answer (NOT the human label!)
    #       and return a validated JudgeResult
    raise NotImplementedError
