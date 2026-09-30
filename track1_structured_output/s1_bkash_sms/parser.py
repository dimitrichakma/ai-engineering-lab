from pathlib import Path

from pydantic import ValidationError

from common.llm import generate_json
from .models import Transaction

DATA = Path(__file__).parent / "data" / "sms_samples.txt"

SYSTEM = (
    # TODO: write the system instructions. Tell the model:
    #  - it extracts data from Bangladeshi mobile money SMS
    #  - use null when a value is not in the message; never guess
    #  - amounts are numbers without "Tk" or commas
    ""
)


def parse_sms(sms: str, max_attempts: int = 2) -> tuple[Transaction | None, int]:
    """Return (transaction or None, attempts used)."""
    # TODO 1: build a prompt that contains the SMS.
    # TODO 2: loop up to max_attempts:
    #           raw = generate_json(prompt, Transaction.model_json_schema(), SYSTEM)
    #           try Transaction.model_validate_json(raw) and return it
    #           on ValidationError: print the error and try again
    # TODO 3: if all attempts fail, return (None, max_attempts)
    raise NotImplementedError


def main() -> None:
    lines = [l.strip() for l in DATA.read_text(encoding="utf-8").splitlines() if l.strip()]
    # TODO 4: parse every line, print each result,
    #         then print a summary: "parsed X/Y, retries used Z"


if __name__ == "__main__":
    main()
