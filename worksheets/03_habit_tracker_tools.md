# Worksheet 3: Tools and user scoping · habit tracker `src/tools.py`

Look at: `resolve_user_id_from_thread_id`, `_current_user_id`, `_find_habit`,
`_resolve_habit_or_error`, `log_habit`, `delete_habit`, `query_past_behavior`, `_resolve_log_date`.

## Questions
1. Where does a tool get the user id from? Where does that value originally come from (follow it back to `main.py`)?
2. Why must the model never be able to pass a `user_id` argument? Give a concrete attack.
3. What formats of `thread_id` exist, and why does the friction check use a different one?
4. `log_habit` is called for a habit that doesn't exist. What does the model get back: an exception or a string? Why?
5. What happens if the user logs the same habit twice on the same day?
6. What is the `log_date="yesterday"` case for? Which kind of habit needs it?
7. How does `_find_habit` handle a loosely typed habit name? What happens when two habits match?
8. Why does every tool open a DB session in `try` and close it in `finally`?
9. `delete_habit` is dangerous. What protects it in the main agent? Why is it NOT in the MCP server?
10. What does `query_past_behavior` search, and where does that data come from?

## Draw it
"Did my run and skipped the gym": which tools run, in what order, with which arguments.

## Interview answer
"How do you make sure an agent's tools can't touch another user's data?"

## Compare with C1 of the lab
How is your `run_tool(name, args, user_id)` similar to `ToolRuntime`? What does LangChain give you for free that you had to write?
