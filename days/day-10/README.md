# Day 10: Functions with Outputs

## Topic learned

Return values, multiple returns, docstrings, function composition, and a calculator project.

## Why it matters

Returning data lets one function provide a result to another function and makes logic easier to test.

## Small example

```python
def add(first, second):
    """Return the sum of two numbers."""
    return first + second


print(add(2, 3))
```

## Question to revisit

Why is returning a result usually more reusable than printing inside a function?

## Project: Calculator

- **Problem:** perform repeated arithmetic calculations.
- **Features:** choose an operation, calculate a result, continue from the current result, start again.
- **Inputs:** numbers and an operation choice.
- **Output:** calculated results.
- **Out of scope:** scientific functions and expression parsing.
- **Code:** [Calculator Project](Calculator%20Project).

## Completion check

See [notes/day-10.md](../../notes/day-10.md) for the learning record.