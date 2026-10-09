# Day 7: Hangman Project

## Topic learned

Using functions, loops, lists, strings, and changing game state in a larger program.

## Why it matters

The project combines earlier basics into a complete flow with setup, repeated turns, and an ending condition.

## Small example

```python
letters = ["_", "_", "_"]
letters[0] = "c"
print(" ".join(letters))
```

## Question to revisit

Which parts of a game should be isolated into separate functions?

## Project: Hangman

- **Problem:** let a player guess a hidden word before running out of attempts.
- **Features:** choose a word, accept guesses, reveal matching letters, track lives, show win or loss.
- **Inputs:** guessed letters.
- **Output:** visible word progress and game result.
- **Out of scope:** online multiplayer and persistent player accounts.
- **Code:** [Hangman Project](Hangman%20Project).

## Completion check

See [notes/day-07.md](../../notes/day-07.md) for the project reflection.