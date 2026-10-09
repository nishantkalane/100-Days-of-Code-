# Day 15: Coffee Machine

## Topic learned

Nested dictionaries, functions, resource state, payment handling, validation, and transaction flow.

## Why it matters

The program models a small real-world system where an action should change resources only after validation succeeds.

## Small example

```python
menu = {"espresso": {"cost": 1.5}}
drink = "espresso"
print(menu[drink]["cost"])
```

## Question to revisit

How can classes separate inventory, payment, and drink preparation?

## Project: Coffee Machine

- **Problem:** process drink orders and manage ingredients and money.
- **Features:** select a drink, check resources, accept coins, return change, update inventory, report status.
- **Inputs:** drink commands and coin counts.
- **Output:** drink, change, errors, and resource reports.
- **Out of scope:** a graphical interface, card payments, and persistent inventory.
- **Code:** [Coffee Machine Project](Coffee%20Machine%20Project).

## Completion check

See [notes/day-15.md](../../notes/day-15.md) for the learning record.