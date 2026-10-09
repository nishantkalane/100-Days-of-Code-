# Day 12: Scope and Number Guessing

## Learned

- Local variables belong to the function that creates them.
- Global constants can represent shared configuration, but mutable globals create hidden coupling.
- Namespaces prevent unrelated names from colliding.
- A guessing game combines random data, loops, conditions, and state.

## Topics in plain language

- **Local variable:** a name that belongs only inside its function.
- **Global variable:** a name available across a wider part of the program.
- **Constant:** a value intended to stay unchanged, usually written in uppercase.
- **Namespace:** the group of names managed by a particular part of a program.
- **Mutable:** able to change after creation.
- **Hidden coupling:** when code depends on shared state in a way that is easy to miss.

## Practice record

Built Number Guessing and practiced global/local scope examples.

## Small example

```python
attempts = 0

def make_attempt():
	attempts = 1
	return attempts


print(make_attempt())
print(attempts)
```

The `attempts` inside the function is local; it does not replace the variable outside it.

## Technical Python practice

Practiced local and global lookup rules, constants by naming convention, and passing values instead of changing global state.

```python
TARGET = 7


def is_correct(guess: int) -> bool:
	return guess == TARGET


print(is_correct(7))
```

## Next review

Pass state into functions rather than relying on mutable global variables.

## What went wrong or remains unclear

Global mutable values can be changed from many places and make behavior harder to predict. Passing values explicitly makes dependencies visible.