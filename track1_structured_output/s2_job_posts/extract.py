import csv
from pathlib import Path

from pydantic import ValidationError

from common.llm import generate_json
from .models import JobPost

DATA_DIR = Path(__file__).parent / "data"
OUT_CSV = Path(__file__).parent / "jobs.csv"

SYSTEM = "Extract job inforamtion from given description, Never invent values, use null instead. Never guess"  


def extract_job(text: str) -> JobPost:
    error = None
    for _ in range(3):
        raw = generate_json(text, JobPost.model_json_schema(), SYSTEM)
        try:
            return JobPost.model_validate_json(raw)
        except ValidationError as e:
            error = e
    raise error  # re-raise the last error if all attempts fail        
    


def to_row(job: JobPost) -> dict:
    return {
        "title": job.title,
        "company": job.company,
        "work_mode": job.work_mode,
        "location": job.location,
        "salary_min": job.salary.min_bdt if job.salary else None,
        "salary_max": job.salary.max_bdt if job.salary else None,
        "must_have": "; ".join(i.skill for i in job.requirements if i.required),
        "nice_to_have": "; ".join(i.skill for i in job.requirements if not i.required),
    }

def main() -> None:
    jobs = [to_row(extract_job(p.read_text())) for p in sorted(DATA_DIR.glob("job_*.txt"))]
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames= jobs[0].keys())
        writer.writeheader()
        writer.writerows(jobs)
     


if __name__ == "__main__":
    main()
