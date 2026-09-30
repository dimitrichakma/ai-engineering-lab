"""Chat logic with no Streamlit inside, so pytest can test it."""
from collections.abc import Callable, Iterable

ROLES = {"user", "assistant"}


def new_state() -> dict:
    # TODO: return {"messages": [], "stopped": False}
    raise NotImplementedError


def add_message(state: dict, role: str, content: str) -> None:
    # TODO: validate role (ValueError if not in ROLES), then append {"role": role, "content": content}
    raise NotImplementedError


def trim_history(messages: list[dict], max_messages: int) -> list[dict]:
    # TODO: keep a leading system message (if present) + the last `max_messages` other messages
    raise NotImplementedError


def collect_stream(chunks: Iterable[str], should_stop: Callable[[], bool]) -> tuple[str, bool]:
    # TODO: check should_stop() BEFORE taking each chunk; stop early and return (text_so_far, True)
    #       otherwise return (full_text, False)
    raise NotImplementedError


def retry_last(state: dict) -> str | None:
    # TODO: if the last message is from the assistant, remove it.
    #       Return the content of the last user message, or None if there is none.
    raise NotImplementedError


def fake_stream(text: str = "This is a fake streamed reply from the lab.") -> Iterable[str]:
    """Given. Yields word by word, for running the UI without a model."""
    import time

    for word in text.split():
        time.sleep(0.05)
        yield word + " "
