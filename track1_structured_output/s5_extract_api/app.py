import logging
from typing import Callable

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError

from common.llm import generate_json
from track1_structured_output.s2_job_posts.models import JobPost

logging.basicConfig(filename="failures.log", level=logging.WARNING)
log = logging.getLogger("extract_api")

app = FastAPI(title="Extraction API")

Generator = Callable[[str, dict, str | None], str]


class ExtractRequest(BaseModel):
    # TODO: text field with min_length=20 and max_length=8000
    pass


def get_generator() -> Generator:
    """Dependency. Tests replace this with a fake."""
    return generate_json


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/extract/job", response_model=JobPost)
def extract_job(body: ExtractRequest, generate: Generator = Depends(get_generator)) -> JobPost:
    # TODO 1: build the prompt from body.text (you can import SYSTEM from track1_structured_output.s2_job_posts.extract)
    # TODO 2: up to 2 attempts: raw = generate(prompt, JobPost.model_json_schema(), SYSTEM)
    #         then JobPost.model_validate_json(raw)
    # TODO 3: on final failure: log.warning(...) with the raw output,
    #         then raise HTTPException(status_code=502, detail="model output invalid")
    raise NotImplementedError
