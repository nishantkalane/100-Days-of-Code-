# Day 15: Coffee Machine

## Learned

- Nested dictionaries can represent a menu and its ingredients.
- A stateful program must update resources only after a successful transaction.
- Validation should happen before money or resources are changed.
- Functions make resource checks, payment, and reporting easier to inspect.

## Topics in plain language

- **Stateful program:** a program that remembers information between actions.
- **Inventory:** the resources currently available.
- **Transaction:** one complete exchange, such as paying for a drink.
- **Validation:** checking that input or state is acceptable before acting.
- **Side effect:** a change outside a function's local calculation, such as reducing water.
- **Separation of concerns:** keeping menu data, payment logic, and resource updates distinct.

## Practice record

Built a command-line Coffee Machine with drinks, resources, payments, and reports.

## Small example

```python
resources = {"water": 300, "coffee": 100}
recipe = {"water": 50, "coffee": 18}

has_enough = all(resources[item] >= amount for item, amount in recipe.items())
print(has_enough)
```

The recipe and inventory share keys, which lets the program check every required ingredient consistently.

## Technical Python practice

Practiced nested dictionaries, iterating through `.items()`, generator expressions, `all()`, and checking state before mutating it.

```python
resources = {"water": 100, "coffee": 20}
recipe = {"water": 50, "coffee": 18}
can_make = all(resources[name] >= amount for name, amount in recipe.items())
print(can_make)
```

## Next review

Use classes and tests to isolate inventory, payment, and drink preparation behavior.

## What went wrong or remains unclear

Resources must not be deducted before payment and availability are confirmed. This transaction order is the key behavior to protect with tests.