# C11: Document ingestion (PDF → clean chunks)

**Time:** 1 to 2 evenings · **Why:** real RAG breaks on messy PDFs long before the LLM matters.
You will hit this in Somajji Phase 1 with the WHO guides, so learn it here first.

## The problem
`data/clinic_guide.pdf` is a small made up 4 page PDF with real world mess:
- a **header** and **footer** repeated on every page ("Internal use only", "Page 3 of 4")
- a **table** of services and fees on page 3, which turns into jumbled text if you extract it naively
- section headings you want to keep as metadata

Open the PDF and look at it first. Then run plain `pypdf` text extraction and look at the output.

## What you write in `ingest.py`
1. `extract_pages(path) -> list[Page]`: page number + text, using `pdfplumber`.
2. `find_repeated_lines(pages, min_share=0.75) -> set[str]`: lines that appear on most pages
   (after replacing digits, so "Page 1 of 4" and "Page 2 of 4" count as the same line).
3. `clean_page(text, repeated) -> str`: remove those lines and extra blank lines.
4. `table_to_markdown(rows) -> str`: turn a table (`page.extract_tables()`) into a markdown table,
   so the model sees clear columns. Replace the jumbled table text on that page with it.
5. `chunk_pages(pages, max_words) -> list[Chunk]`: chunks never span pages; each chunk keeps
   `page`, `section` (the latest heading seen) and `source`.
6. `main()`: print every chunk with its metadata.

## Done when
- [ ] No chunk contains "Internal use only" or "Page 3 of 4".
- [ ] The fees table appears as a markdown table in exactly one chunk, with page 3.
- [ ] Every chunk has a page and a section (tested).
- [ ] The pure functions (2, 3, 4, 5) are unit tested without opening a PDF.

## Stretch
- Add a real public PDF you care about (for example one WHO guide for Somajji) and see what breaks.
- Scanned PDFs have no text layer. How would you detect that and what would you do?
