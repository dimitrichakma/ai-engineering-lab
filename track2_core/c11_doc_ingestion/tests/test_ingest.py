from track2_core.c11_doc_ingestion.ingest import (Page, chunk_pages, clean_page,
                                                  find_repeated_lines, table_to_markdown)

HEADER = "Green Hills Clinic Guide"


def pages():
    return [
        Page(number=1, text=f"{HEADER}\n1. Intro\nhello world\nPage 1 of 3"),
        Page(number=2, text=f"{HEADER}\nmore intro text\nPage 2 of 3"),
        Page(number=3, text=f"{HEADER}\n2. Fees\nfees are low\nPage 3 of 3"),
    ]


def test_find_repeated_lines_handles_page_numbers():
    rep = find_repeated_lines(pages())
    assert HEADER in rep
    assert "Page # of #" in rep
    assert "hello world" not in rep


def test_clean_page_removes_header_and_footer():
    rep = find_repeated_lines(pages())
    out = clean_page(pages()[0].text, rep)
    assert HEADER not in out and "Page 1" not in out
    assert "hello world" in out


def test_table_to_markdown():
    md = table_to_markdown([["Service", "Fee"], ["Vaccination", None]])
    assert md.splitlines()[0].startswith("| Service")
    assert "---" in md.splitlines()[1]
    assert "| Vaccination |" in md


def test_chunks_keep_page_and_carry_section():
    cleaned = [Page(number=p.number, text=clean_page(p.text, find_repeated_lines(pages())))
               for p in pages()]
    chunks = chunk_pages(cleaned, max_words=50)
    by_page = {c.page: c for c in chunks}
    assert by_page[2].section.startswith("1. Intro")     # carried over from page 1
    assert by_page[3].section.startswith("2. Fees")

# TODO: a chunk never contains text from two pages (make a long page and a small max_words)
