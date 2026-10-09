# Day 16: Object-Oriented Programming

## Goal

Move from small scripts to a program whose data and behavior are organized into objects.

## Learned

- A class describes the shared structure and behavior of a type of object.
- An instance is one concrete object created from that class.
- Methods can validate or change an object's own state.
- Small classes can collaborate without putting every variable in global scope.

## Concepts to practice

- Classes define a type of object.
- `__init__` establishes object state.
- Methods describe behavior that operates on that state.
- Encapsulation keeps related data and operations together.
- Objects can collaborate without one giant global script.

## Topics in plain language

- **Class:** a blueprint describing what a kind of object knows and can do.
- **Object:** one concrete thing created from a class.
- **Attribute:** data stored on an object.
- **Method:** a function that belongs to a class.
- **Constructor:** the setup method that creates an object's initial state.
- **Encapsulation:** keeping related data and behavior together and controlling how they are used.
- **Instance:** one individual object made from a class.

## Project plan

Build a small library manager, quiz game, or banking system in `days/day-16/project`.

## Small example

```python
class Counter:
	def __init__(self):
		self.value = 0

	def increment(self):
		self.value += 1


counter = Counter()
counter.increment()
print(counter.value)
```

The object stores its own state, and the method changes that state. This is the basic pattern to expand into a useful project.

## Technical Python practice

Practiced class definitions, the `__init__` method, instance attributes, `self`, and instance methods.

```python
class User:
	def __init__(self, name: str):
		self.name = name

	def introduce(self) -> str:
		return f"My name is {self.name}."


user = User("Ada")
print(user.introduce())
```

## Definition of done

Create at least two classes, validate user input, keep the entry point small, and add tests for the most important behavior.

## Practice record

The Day 16 project scaffold is ready in `days/day-16/project`; the independent project implementation is the next coding step.

## What went wrong or remains unclear

The project idea and class boundaries still need to be chosen before implementation. That is the first design decision for Day 16.

## Next review

Choose one small problem, identify its nouns as possible classes, and implement the smallest useful interaction between two objects.