# Day 1: Foundations

## Learned

- Programs execute instructions in order.
- Variables give names to values and make later changes easier.
- `input()` returns text, even when the user enters a number.
- Strings can be combined with concatenation or f-strings.
- Clear names make a short program easier to understand.

## Topics in plain language

- **Variable:** a labeled box that stores a value.
- **String:** text made from characters.
- **Input:** information the user gives to the program.
- **Output:** information the program shows back to the user.
- **Expression:** a piece of code that produces a value, such as `2 + 3`.
- **Syntax:** the grammar rules Python expects.

## Practice record

Built small input/output exercises and the Band Name Generator.

## Small example

```python
city = input("Where do you live? ")
pet = input("What is your pet's name? ")
print(f"Your band name could be {city} {pet}.")
```

`input()` gives the program text. The f-string inserts those values into the output.

## Technical Python practice

Practiced variable assignment, calling built-in functions, reading strings with `input()`, and formatted string literals.

```python
name = "Ada"
language = "Python"
print(f"{name} is learning {language}.")
```

## Next review

Practice converting input and writing a small function instead of placing everything at the top level.

## What went wrong or remains unclear

The main beginner risk was treating all input as numbers or assuming the user will always enter useful text. Input validation is a next improvement.