from pathlib import Path

from pydantic import ValidationError

from common.llm import generate_json
from .models import MeetingSummary

DATA_DIR = Path(__file__).parent / "data"
SYSTEM = ""  # TODO


def first_prompt(notes: str) -> str:
    # TODO
    raise NotImplementedError


def repair_prompt(notes: str, bad_json: str, error: ValidationError) -> str:
    """Ask the model to fix its own answer.

    Include: the original notes, the JSON it returned, and the error text.
    Tip: str(error) is readable; error.errors() gives a list you can format nicely.
    """
    # TODO
    raise NotImplementedError


def extract(notes: str, max_attempts: int = 3) -> tuple[MeetingSummary, int]:
    """Return (summary, attempts used). Raise the last error if all attempts fail."""
    # TODO: first_prompt -> generate_json -> validate
    #       on error: print it, build repair_prompt, try again
    raise NotImplementedError


def main() -> None:
    for path in sorted(DATA_DIR.glob("notes_*.txt")):
        # TODO: extract and print the summary and the number of attempts
        pass


if __name__ == "__main__":
    main()
