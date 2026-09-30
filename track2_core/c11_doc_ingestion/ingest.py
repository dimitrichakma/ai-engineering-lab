import re
from collections import Counter
from pathlib import Path

from pydantic import BaseModel

DATA = Path(__file__).parent / "data" / "clinic_guide.pdf"
HEADING_RE = re.compile(r"^\d+\.\s+\S")   # "3. Services and fees"


class Page(BaseModel):
    number: int
    text: str
    tables: list[list[list[str | None]]] = []


class Chunk(BaseModel):
    text: str
    page: int
    section: str
    source: str


def extract_pages(path: Path) -> list[Page]:
    # TODO: import pdfplumber; for each page: Page(number=i, text=page.extract_text() or "",
    #       tables=page.extract_tables())
    raise NotImplementedError


def normalize(line: str) -> str:
    """Given. 'Page 3 of 4' -> 'Page # of #' so repeated footers look the same."""
    return re.sub(r"\d+", "#", line.strip())


def find_repeated_lines(pages: list[Page], min_share: float = 0.75) -> set[str]:
    """Return NORMALIZED lines that appear on at least min_share of the pages."""
    # TODO: count each normalized line once per page
    raise NotImplementedError


def clean_page(text: str, repeated: set[str]) -> str:
    # TODO: drop lines whose normalized form is in `repeated`; strip; no double blank lines
    raise NotImplementedError


def table_to_markdown(rows: list[list[str | None]]) -> str:
    """First row = header. None cells become empty strings."""
    # TODO
    raise NotImplementedError


def chunk_pages(pages: list[Page], max_words: int = 120, source: str = "clinic_guide.pdf") -> list[Chunk]:
    """Chunks never span pages. `section` = the latest heading line seen so far (carry it across pages)."""
    # TODO
    raise NotImplementedError


def main() -> None:
    # TODO: extract -> find repeated -> clean each page -> replace table text with markdown
    #       (hint: remove the lines of the page that belong to the table, then append the markdown)
    #       -> chunk -> print each chunk with page and section
    pass


if __name__ == "__main__":
    main()
