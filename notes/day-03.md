# Day 3: Control Flow

## Learned

- `if`, `elif`, and `else` express branching decisions.
- Comparisons produce Boolean values.
- Logical operators combine conditions.
- `%` is useful for divisibility and repeating patterns.
- Nested decisions work, but too much nesting makes code harder to maintain.

## Topics in plain language

- **Condition:** a question that can be true or false.
- **Boolean:** a value that is either `True` or `False`.
- **Comparison:** checking values with operators such as `==`, `<`, or `>`.
- **Branch:** one possible route through a program.
- **Logical operator:** a word such as `and`, `or`, or `not` that combines or reverses conditions.
- **Modulo:** the remainder left after division; useful for repeating cycles.

## Practice record

Built Treasure Island and practiced pizza, modulo, and conditional exercises.

## Small example

```python
age = int(input("Age: "))

if age < 13:
	category = "child"
elif age < 20:
	category = "teenager"
else:
	category = "adult"

print(category)
```

The branches are checked from top to bottom, and only the first matching branch runs.

## Technical Python practice

Practiced comparison operators, Boolean expressions, chained `if` statements, and combining conditions with `and`.

```python
temperature = 22
is_comfortable = temperature >= 18 and temperature <= 26
print("comfortable" if is_comfortable else "uncomfortable")
```

## Next review

Replace deeply nested decisions with small functions or clearer early exits.

## What went wrong or remains unclear

Nested conditions can become difficult to follow when several rules interact. Writing the possible branches down first makes missing outcomes easier to find.