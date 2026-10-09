# Day 2: Data and Arithmetic

## Learned

- Python has different data types with different operations.
- `int()`, `float()`, and `str()` convert values explicitly.
- Arithmetic operators follow normal precedence rules.
- Rounding and formatting matter when displaying money.

## Topics in plain language

- **Data type:** the kind of value something is, such as text, a whole number, or a decimal.
- **Integer (`int`):** a whole number with no decimal part.
- **Float (`float`):** a number that can contain a decimal part.
- **Conversion:** changing a value from one type to another.
- **Operator:** a symbol that performs an action, such as `+`, `*`, or `/`.
- **Type error:** Python telling you that an operation does not fit the value's type.

## Practice record

Built a Tip Calculator and exercises for numeric manipulation and type errors.

## Small example

```python
bill = float(input("Bill: "))
people = int(input("People: "))
tip = bill * 0.15
share = (bill + tip) / people
print(f"Each person pays ${share:.2f}")
```

Convert input at the boundary, then keep the calculation working with numbers.

## Technical Python practice

Practiced explicit type conversion with `int()` and `float()`, arithmetic precedence, and numeric formatting with a precision specifier.

```python
price = float("12.5")
quantity = int("3")
total = price * quantity
print(f"Total: ${total:.2f}")
```

## Next review

Validate numeric input and decide where rounding should happen in a calculation.

## What went wrong or remains unclear

Text from `input()` cannot be used in arithmetic until it is converted. Invalid numeric text and division by zero still need deliberate handling.