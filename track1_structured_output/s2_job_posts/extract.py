import csv
from pathlib import Path

from pydantic import ValidationError

from common.llm import generate_json
from .models import JobPost

DATA_DIR = Path(__file__).parent / "data"
OUT_CSV = Path(__file__).parent / "jobs.csv"

SYSTEM = ""  # TODO: instructions. Include the "never invent values, use null" rule.


def extract_job(text: str) -> JobPost:
    # TODO: call generate_json with JobPost's schema and validate the result.
    #       Reuse your retry idea from S1.
    raise NotImplementedError


def to_row(job: JobPost) -> dict:
    # TODO: flatten the nested object into one flat dict for the CSV.
    #       Example keys: title, company, work_mode, salary_min, salary_max, must_have, nice_to_have
    raise NotImplementedError


def main() -> None:
    jobs = []
    for path in sorted(DATA_DIR.glob("job_*.txt")):
        # TODO: extract, print, and collect each job
        pass
    # TODO: write OUT_CSV with csv.DictWriter


if __name__ == "__main__":
    main()
