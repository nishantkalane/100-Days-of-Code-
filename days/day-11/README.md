# Day 11: Blackjack Project

## Topic learned

Combining functions, lists, random data, game rules, turns, scoring, and project-sized decomposition.

## Why it matters

A complete project requires keeping rules, state changes, user interaction, and the main loop understandable.

## Small example

```python
def hand_value(cards):
    return sum(cards)


print(hand_value([10, 7]))
```

## Question to revisit

How can scoring rules be tested without running the whole game?

## Project: Blackjack

- **Problem:** play a simplified card game against a dealer.
- **Features:** deal cards, calculate scores, handle turns, detect busts, announce the result.
- **Inputs:** player decisions such as drawing another card.
- **Output:** hands, scores, and a win or loss result.
- **Out of scope:** online play, betting, and a full casino rules engine.
- **Code:** [Blackjack Project](Blackjack%20Project).

## Completion check

See [notes/day-11.md](../../notes/day-11.md) for the learning record.