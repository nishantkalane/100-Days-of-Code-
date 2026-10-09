# Day 5: Loops

## Topic learned

For loops, ranges, repeated work, running totals, highest values, and random password generation.

## Why it matters

Loops remove duplication when the same operation needs to happen for many values.

## Small example

```python
total = 0
for number in range(1, 4):
    total += number
print(total)
```

## Question to revisit

When is a `for` loop better than a `while` loop?

## Project: Password Generator

- **Problem:** create a random password from requested character groups.
- **Features:** choose letters, symbols, and numbers; generate characters; combine them into a password.
- **Inputs:** requested counts for each character group.
- **Output:** one generated password.
- **Out of scope:** password storage and account management.
- **Code:** [Password Generator Project](Password%20Generator%20Project).

## Completion check

The loop exercises and project are preserved. See [notes/day-05.md](../../notes/day-05.md).