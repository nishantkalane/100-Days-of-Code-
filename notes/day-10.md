# Day 10: Return Values and Documentation

## Learned

- Returning data makes functions composable and testable.
- Multiple values can be returned together and unpacked by the caller.
- Docstrings explain a function's purpose and expected behavior.
- A calculator is easier to extend when operators map to functions.

## Topics in plain language

- **Return:** sending a result from a function back to its caller.
- **Tuple:** a fixed group of values that can be returned and unpacked together.
- **Unpacking:** assigning each item in a group to its own variable.
- **Docstring:** a description written inside a function, class, or module.
- **Composition:** building a larger operation by combining smaller functions.
- **Pure function:** a function whose result depends only on its inputs and does not change outside state.

## Practice record

Built Calculator and practiced output functions, multiple returns, and docstrings.

## Small example

```python
def divide(dividend, divisor):
	"""Return the quotient and remainder."""
	return dividend // divisor, dividend % divisor


quotient, remainder = divide(17, 5)
print(quotient, remainder)
```

Returning values keeps a function useful to other code instead of making it only print.

## Technical Python practice

Practiced tuple return values, unpacking, docstrings, and integer division with `//` alongside the remainder operator `%`.

```python
def quotient_and_remainder(value: int, divisor: int) -> tuple[int, int]:
	return value // divisor, value % divisor


quotient, remainder = quotient_and_remainder(10, 3)
print(quotient, remainder)
```

## Next review

Write tests for each operation and define behavior for invalid operators and division by zero.

## What went wrong or remains unclear

A calculator can fail at the boundaries even when normal arithmetic works. Invalid operators and zero divisors need explicit behavior.