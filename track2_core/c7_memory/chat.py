"""A tiny command line chat with summary memory. Type 'quit' to stop."""
from common.llm import generate_text

from .memory import SummaryMemory, message_tokens

SYSTEM = "You are a friendly study buddy. Keep answers short."


def llm_summarize(old_summary: str, messages: list[dict]) -> str:
    # TODO: ask generate_text to update old_summary with the facts in `messages`
    #       in at most 3 sentences. Keep names, numbers and decisions.
    raise NotImplementedError


def main() -> None:
    memory = SummaryMemory(SYSTEM, max_recent_tokens=300, summarize_fn=llm_summarize)
    while True:
        text = input("you> ").strip()
        if text == "quit":
            break
        # TODO: add the user message, build the prompt from memory.context(),
        #       call the model, add the reply, print it and the tokens sent this turn


if __name__ == "__main__":
    main()
