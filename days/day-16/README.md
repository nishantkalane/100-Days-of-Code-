# Day 16

## Focus

Object-oriented programming and the first project built independently from the course exercise.

## Why it matters

Classes let a program keep related data and behavior together, which becomes useful as projects grow beyond one small script.

## Small example

```python
class Book:
	def __init__(self, title: str):
		self.title = title


book = Book("Python Basics")
print(book.title)
```

## Question to investigate

Which responsibilities should become classes, and which should remain simple functions?

## Project goal

Build a small system with at least two classes, object interaction, methods, and input validation. Good choices include a library manager, quiz game, or simple banking system.

## First-version scope

- **Problem:** organize a small real-world system with objects.
- **Features:** create objects, change object state through methods, validate input, display a result.
- **Inputs:** simple command-line values.
- **Output:** a useful result from interacting objects.
- **Out of scope:** databases, web interfaces, authentication, and deployment.

## Files for this day

- [Project](project): the independent Day 16 application.
- [Learning note](../../notes/day-16.md): concepts, terminology, examples, and reflection.

## Definition of done

- The project runs from a clear entry point.
- The README explains the problem and how to run it.
- Invalid input is handled without crashing.
- The core behavior has a few focused tests.
- A short learning note records the concepts practiced.

For the repeatable process, use the [daily workflow](../../DAILY_CHECKLIST.md).