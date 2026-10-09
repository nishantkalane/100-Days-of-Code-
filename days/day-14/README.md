# Day 14: Higher or Lower

## Topic learned

Game loops, functions, dictionary data, comparisons, score state, and separating data from rules.

## Why it matters

This project combines earlier fundamentals into a repeated game with changing state and a clear ending condition.

## Small example

```python
def higher(first, second):
    return first > second


print(higher(100, 50))
```

## Question to revisit

How can the comparison rule be tested independently of user input?

## Project: Higher or Lower

- **Problem:** guess which account has the higher value.
- **Features:** show two choices, accept a guess, compare values, track score, continue after correct guesses.
- **Inputs:** a comparison choice.
- **Output:** correctness feedback and score.
- **Out of scope:** live data retrieval and online rankings.
- **Code:** [Higher or Lower Project](Higher%20or%20Lower%20Project).

## Completion check

See [notes/day-14.md](../../notes/day-14.md) for the learning record.