# Day 11: Blackjack Project

## Learned

- A project needs explicit rules before implementation.
- Lists model a hand of cards and functions can isolate scoring rules.
- Randomized behavior needs careful testing and repeatable small units.
- A game loop should clearly separate setup, turns, and final scoring.

## Topics in plain language

- **State:** the information that changes while the program runs.
- **Game loop:** the repeated cycle that handles turns until an ending condition occurs.
- **Rule:** a condition that determines what the program should allow or calculate.
- **Decomposition:** breaking one large problem into smaller jobs.
- **Edge case:** an unusual input or situation that still needs correct behavior.
- **Testable unit:** a small part of code that can be checked independently.

## Practice record

Built a command-line Blackjack game and practiced project-sized decomposition.

## Small example

```python
def hand_value(cards):
	"""Return the total value of a hand."""
	return sum(cards)


player_hand = [10, 7]
print(hand_value(player_hand))
```

Keeping scoring in a function makes the rule easier to test separately from the game loop.

## Technical Python practice

Practiced list processing, `sum()`, function decomposition, and passing a collection into a function.

```python
def total_score(cards: list[int]) -> int:
	return sum(cards)


print(total_score([10, 6, 4]))
```

## Next review

Extract scoring into a pure function and test aces, blackjack, and bust conditions.

## What went wrong or remains unclear

Card scoring has edge cases, especially when an ace can have more than one value. The scoring rule should be tested independently from random dealing.