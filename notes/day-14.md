# Day 14: Higher or Lower

## Learned

- A game can be represented as repeated rounds over changing state.
- Data and game rules are easier to maintain when they are separated.
- A score is state that should change only after a correct comparison.
- Functions keep the main loop readable.

## Topics in plain language

- **Comparison function:** a function that decides which value or option should win.
- **Loop condition:** the rule that decides whether another round should happen.
- **Score:** stored information representing progress or success.
- **Data separation:** keeping facts, such as account data, apart from rules that use them.
- **Control flow:** the order in which instructions are executed.
- **Invariant:** a fact that should remain true while the program runs.

## Practice record

Built Higher or Lower using account data, comparisons, and a score loop.

## Small example

```python
def higher_value(first, second):
	return first if first > second else second


score = 0
if higher_value(120, 80) == 120:
	score += 1
print(score)
```

Returning the result of a comparison keeps the score update separate from the game rule.

## Technical Python practice

Practiced functions that return values, conditional expressions, mutable score state, and repeating a game turn with a `while` loop.

```python
score = 0
playing = True
while playing:
	score += 1
	playing = False
print(score)
```

## Next review

Write a comparison function with explicit inputs and return values before adding new features.

## What went wrong or remains unclear

The main loop can become responsible for data lookup, comparison, scoring, and display at the same time. Separating those responsibilities will make later changes easier.