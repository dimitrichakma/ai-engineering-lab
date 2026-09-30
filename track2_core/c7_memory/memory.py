import math
from typing import Callable

Message = dict  # {"role": "system" | "user" | "assistant" | "tool", "content": str}


def count_tokens(text: str) -> int:
    # TODO: approximate: ceil(len(text) / 4)
    raise NotImplementedError


def message_tokens(m: Message) -> int:
    return count_tokens(m["content"]) + 4   # +4 for role and formatting overhead


def trim_history(messages: list[Message], max_tokens: int) -> list[Message]:
    """Keep system messages + the newest non-system messages that fit in max_tokens
    (system messages NOT counted). The kept part must start with a "user" message."""
    # TODO 1: separate system messages from the rest
    # TODO 2: walk the rest from the END, adding whole messages while they fit
    # TODO 3: drop from the FRONT of the kept part until it starts with role "user"
    # TODO 4: return system messages + kept part
    raise NotImplementedError


class SummaryMemory:
    def __init__(self, system_prompt: str, max_recent_tokens: int,
                 summarize_fn: Callable[[str, list[Message]], str]):
        self.system = {"role": "system", "content": system_prompt}
        self.max_recent_tokens = max_recent_tokens
        self.summarize_fn = summarize_fn
        self.summary = ""
        self.recent: list[Message] = []

    def add(self, message: Message) -> None:
        # TODO: append; then while recent is over budget, move the OLDEST user+assistant pair
        #       into the summary with summarize_fn(self.summary, [those messages])
        raise NotImplementedError

    def context(self) -> list[Message]:
        # TODO: system, then the summary as a system message (only if not empty), then recent
        raise NotImplementedError
