# Day 13: Debugging

## Learned

- Reproducing a bug is the first step toward fixing it reliably.
- Print statements reveal assumptions about values and control flow.
- A debugger can inspect variables while execution is paused.
- The smallest failing example is often easier to reason about than the full program.

## Topics in plain language

- **Bug:** behavior in a program that is wrong or unexpected.
- **Debugging:** finding and correcting the cause of a bug.
- **Reproduction:** making a bug happen again reliably.
- **Breakpoint:** a pause placed in code so its state can be inspected.
- **Traceback:** Python's report showing where an error happened.
- **Assertion:** a statement that checks an assumption and reports when it is false.

## Practice record

Practiced describing problems, reproducing bugs, fixing errors, and using a debugger.

## Small example

```python
def average(total, count):
	if count == 0:
		raise ValueError("count must be greater than zero")
	return total / count


print(average(10, 2))
```

An explicit check turns a vague runtime failure into a clear statement of the invalid input.

## Technical Python practice

Practiced raising a specific exception, guarding invalid input early, and reading tracebacks to locate the failing line.

```python
def percentage(part: float, whole: float) -> float:
	if whole == 0:
		raise ValueError("whole must not be zero")
	return part / whole * 100


print(percentage(1, 4))
```

## Next review

When debugging, write the expected value and actual value before changing code.

## What went wrong or remains unclear

Changing several lines at once can hide the real cause of a bug. Reproducing one failure and making one focused change gives clearer evidence.