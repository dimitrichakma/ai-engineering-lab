"""CI eval gate. Reads SAVED predictions (no model call) and fails if accuracy drops.

1. Run your S3 triage once locally and save predictions to saved_predictions.json:
   [{"id": "1", "category": "delivery"}, ...]
2. Put the minimum accuracy (for example 0.75) in eval_threshold.txt.
3. CI runs this file. Exit code 1 = red build.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
GOLD = HERE.parents[1] / "track1_structured_output" / "s3_ticket_triage" / "data" / "tickets.csv"


def main() -> int:
    # TODO: load gold labels from GOLD, predictions from saved_predictions.json,
    #       compute category accuracy, read the threshold, print both,
    #       return 0 if accuracy >= threshold else 1
    _ = (json, GOLD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
