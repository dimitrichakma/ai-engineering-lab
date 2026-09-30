from .store import BOOKS


def add_book(user_id: int, title: str) -> str:
    # TODO: add the title for this user with 0 pages (don't overwrite if it exists)
    raise NotImplementedError


def log_pages(user_id: int, title: str, pages: int) -> str:
    # TODO: add pages to the book. Book not found -> return a helpful message, don't raise.
    #       pages <= 0 -> return an error message.
    raise NotImplementedError


def reading_summary(user_id: int) -> str:
    # TODO: one line per book: "Deep Work: 120 pages". No books -> say so.
    raise NotImplementedError


# What the MODEL sees. Note: no user_id anywhere in here.
TOOL_SCHEMAS: list[dict] = [
    {
        "type": "function",
        "function": {
            "name": "add_book",
            "description": "Start tracking a new book for the current user.",
            "parameters": {
                "type": "object",
                "properties": {"title": {"type": "string", "description": "Book title"}},
                "required": ["title"],
            },
        },
    },
    # TODO: schema for log_pages (title: string, pages: integer)
    # TODO: schema for reading_summary (no parameters)
]


def run_tool(name: str, arguments: dict, user_id: int) -> str:
    """Run the named tool for `user_id`. Never raise: return an error string instead."""
    # TODO: map names to functions. Call with user_id + **arguments.
    #       Unknown name -> "Unknown tool: <name>"
    #       TypeError (wrong/missing arguments) -> "Bad arguments for <name>: <error>"
    raise NotImplementedError
