"""Given. A tiny in-memory store: {user_id: {book_title: pages_read}}. Do not change."""

BOOKS: dict[int, dict[str, int]] = {
    1: {"Deep Work": 120},
    2: {"Secret Diary": 45},   # user 2's private data; user 1 must never see this
}


def reset() -> None:
    BOOKS.clear()
    BOOKS.update({1: {"Deep Work": 120}, 2: {"Secret Diary": 45}})
