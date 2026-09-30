def fixed_size(text: str, size_words: int, overlap_words: int) -> list[str]:
    """Split into chunks of `size_words` words; each new chunk starts `size_words - overlap_words`
    words after the previous one. Raise ValueError if overlap >= size."""
    # TODO
    raise NotImplementedError


def by_heading(text: str) -> list[str]:
    """One chunk per '## ' section, INCLUDING the heading line (why include it?).
    Ignore anything before the first '## '."""
    # TODO
    raise NotImplementedError
