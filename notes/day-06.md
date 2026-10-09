# Day 6: Functions

## Learned

- Functions give a name to a reusable block of behavior.
- Parameters allow the same function to work with different values.
- A function should have one clear responsibility.
- Returning a value is different from printing a value.

## Topics in plain language

- **Function:** a named recipe for doing one job.
- **Parameter:** a named input accepted by a function.
- **Argument:** the actual value passed into a function call.
- **Return value:** the result a function gives back.
- **Scope:** the part of a program where a name can be used.
- **Refactoring:** rearranging code to make it clearer without changing its intended behavior.

## Practice record

Practiced functions alongside loops and small interactive programs.

## Small example

```python
def greet(name):
	return f"Hello, {name}!"


message = greet("Python learner")
print(message)
```

The function receives a value, creates a result, and returns it to the caller.

## Technical Python practice

Practiced defining functions, type annotations for parameters and returns, calling functions, and returning values.

```python
def double(number: int) -> int:
	return number * 2


print(double(4))
```

## Next review

Refactor one earlier project so its input, logic, and output are separate functions.

## What went wrong or remains unclear

It is easy to create functions that print instead of return. A function's responsibility and result should be decided before writing its body.