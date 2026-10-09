# Day 4: Collections and Randomness

## Learned

- Lists preserve an ordered collection of values.
- Indexes start at zero and can produce `IndexError` when used incorrectly.
- The `random` module can select values and generate numbers.
- A list can hold reusable game data such as choices or images.

## Topics in plain language

- **List:** an ordered row of values.
- **Element:** one item inside a collection.
- **Index:** the position used to find an item; Python starts counting at zero.
- **Module:** a file or library of code that can be imported and reused.
- **Randomness:** choosing an outcome in a way that cannot be predicted in advance.
- **Exception:** an error event raised while a program is running.

## Practice record

Built Rock Paper Scissors and practiced lists, random selection, and list indexes.

## Small example

```python
import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(computer_choice)
```

The list stores related values, while `random.choice()` selects one valid item for us.

## Technical Python practice

Practiced list literals, zero-based indexing, importing a standard-library module, and calling a module function.

```python
colors = ["red", "green", "blue"]
first_color = colors[0]
print(first_color)
```

## Next review

Move repeated rules into functions and validate indexes before accessing a list.

## What went wrong or remains unclear

An invalid index can stop a program with an exception. User choices should be checked before they are used to access a list.