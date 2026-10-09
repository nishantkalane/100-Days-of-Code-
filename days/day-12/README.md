# Day 12: Scope and Number Guessing

## Topic learned

Local and global scope, constants, namespaces, mutable state, and a number guessing game.

## Why it matters

Understanding where names live prevents accidental changes and makes functions easier to reason about.

## Small example

```python
TARGET = 7


def correct(guess):
    return guess == TARGET
```

## Question to revisit

When should a value be passed into a function instead of stored globally?

## Project: Number Guessing Game

- **Problem:** challenge a player to find a hidden number.
- **Features:** choose difficulty, generate a target, limit attempts, give higher/lower feedback.
- **Inputs:** difficulty and guesses.
- **Output:** feedback, remaining attempts, and the final result.
- **Out of scope:** multiplayer and saved high scores.
- **Code:** [Number Guessing Project](Number%20Guessing%20Project).

## Completion check

See [notes/day-12.md](../../notes/day-12.md) for the learning record.