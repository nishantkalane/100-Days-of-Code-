# Day 7: Hangman Project

## Learned

- A larger program becomes manageable when divided into functions.
- Game state must be updated consistently after every guess.
- Lists and strings can represent the hidden word and visible progress.
- A clear loop condition prevents a game from continuing after it is over.

## Topics in plain language

- **Game state:** the current facts about a game, such as guesses and remaining lives.
- **Iteration:** repeating a turn until the game ends.
- **Placeholder:** a temporary symbol, such as `_`, that represents an unknown value.
- **Membership:** checking whether a value exists in a collection with `in`.
- **Random choice:** selecting one item from a set of possible items.
- **Separation of concerns:** keeping different responsibilities in different functions or files.

## Practice record

Built Hangman with word data, artwork, guesses, and win/loss conditions.

## Small example

```python
word = "python"
visible = ["_"] * len(word)
guess = "p"

for index, letter in enumerate(word):
	if letter == guess:
		visible[index] = letter

print(" ".join(visible))
```

The list represents changing game state while the original word remains unchanged.

## Technical Python practice

Practiced list multiplication, `enumerate()`, conditional mutation of a list, and joining list items into display text.

```python
letters = ["_"] * 3
for position, letter in enumerate("cat"):
	letters[position] = letter
print(" ".join(letters))
```

## Next review

Create a game-state object so the rules do not depend on many global variables.

## What went wrong or remains unclear

Game state changes in several places, so inconsistent updates can cause incorrect win or loss behavior. Centralizing state would make the rules safer.