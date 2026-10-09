# Day 9: Dictionaries and Nested Data

## Learned

- Dictionaries associate keys with values.
- Nested dictionaries and lists model structured data.
- A dictionary can act as a lookup table for a program.
- A loop can collect entries before calculating a final result.

## Topics in plain language

- **Dictionary:** a lookup table that connects a key to a value.
- **Key:** the label used to find a dictionary value.
- **Value:** the information stored under a key.
- **Nested data:** collections placed inside other collections.
- **Iteration over items:** visiting each key and value in turn.
- **Data model:** the shape and organization chosen to represent information in code.

## Practice record

Built Blind Auction and practiced dictionary access and nested collections.

## Small example

```python
scores = {"Ava": 82, "Leo": 91, "Mia": 87}
winner = max(scores, key=scores.get)
print(f"{winner} has the highest score.")
```

The dictionary maps names to scores, and `max()` can compare values selected by a key function.

## Technical Python practice

Practiced dictionary literals, dictionary lookup, `.items()`, generator expressions, and the `key=` argument to `max()`.

```python
prices = {"coffee": 3.5, "tea": 2.0}
most_expensive = max(prices.items(), key=lambda item: item[1])
print(most_expensive)
```

## Next review

Define the shape of input data before writing code that reads deeply nested keys.

## What went wrong or remains unclear

Deep dictionary access becomes fragile when a key is missing or spelled differently. A clear data shape and validation would prevent confusing failures.