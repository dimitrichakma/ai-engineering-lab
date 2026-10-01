from pathlib import Path

from pydantic import ValidationError

from common.llm import generate_json
from .models import Transaction

DATA = Path(__file__).parent / "data" / "sms_samples.txt"

SYSTEM = (
    'You extracts data from Bangladeshi mobile money SMS messages and return one JSON object. '
    'The amount_bdt must be greater than 0. Never guess and never write N/A or unknown. '
    'If the sms does not show fee_bdt, balance_bdt, trx_id, date_text, counterparty, use null for that field. '
    'Amount_bdt, fee_bdt and balance_bdt are plain numbers: no "Tk" or commas.'
    
)


def parse_sms(sms: str, max_attempts: int = 2) -> tuple[Transaction | None, int]:
    """Return (transaction or None, attempts used)."""
    prompt = f"SMS:\n{sms}"
    
    for attempt in range(1, max_attempts + 1):
        raw = generate_json(prompt, Transaction.model_json_schema(), SYSTEM)
        try:
            return Transaction.model_validate_json(raw), attempt
        except ValidationError as e:
            print(f"Attempt {attempt} failed: {e}")
    return None, max_attempts        


def main() -> None:
    lines = [l.strip() for l in DATA.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(parse_sms(lines[0]))


if __name__ == "__main__":
    main()
