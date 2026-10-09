# Day 8: Functions with Inputs and Caesar Cipher

## Topic learned

Function arguments, positional and keyword arguments, string indexes, modular shifts, and iterative project improvement.

## Why it matters

Well-designed functions make transformations reusable and keep the main program understandable.

## Small example

```python
def shift(value, amount=1):
    return value + amount


print(shift(value=4, amount=2))
```

## Question to revisit

When does a keyword argument make a function call clearer?

## Project: Caesar Cipher

- **Problem:** encode and decode text using a letter shift.
- **Features:** accept text, accept a shift, encode, decode, repeat the interaction.
- **Inputs:** message, direction, and shift amount.
- **Output:** transformed text.
- **Out of scope:** strong modern encryption and secure secret storage.
- **Code:** [Caesar Cipher 1](Caesar%20Cipher%201), [2](Caesar%20Cipher%202), and [3](Caesar%20Cipher%203).

## Completion check

The three project iterations are preserved. See [notes/day-08.md](../../notes/day-08.md).