# Day 5: Loops

## Learned

- `for` loops repeat work over a sequence.
- `range()` is useful for a known number of repetitions.
- A running total or best value can be updated inside a loop.
- Random selection inside loops can generate passwords and other data.

## Topics in plain language

- **Loop:** instructions that repeat.
- **Iteration:** one trip through a loop.
- **Counter:** a variable that records how many times something happened.
- **Accumulator:** a variable that gradually collects a result, such as a total.
- **Range:** a generated sequence of numbers used to control repetitions.
- **Algorithm:** a step-by-step recipe for solving a problem.

## Practice record

Built a Password Generator and practiced scores and range-based loops.

## Small example

```python
total = 0

for number in range(1, 6):
	total += number

print(total)
```

The loop repeats five times and updates the running total on each iteration.

## Technical Python practice

Practiced `for` loops, `range(start, stop)`, augmented assignment, and building a result over multiple iterations.

```python
even_numbers = []
for number in range(2, 11, 2):
	even_numbers.append(number)
print(even_numbers)
```

## Next review

Separate generation from display so generated values can be tested without user interaction.

## What went wrong or remains unclear

Random output is difficult to verify by looking at one run. Separating generation from printing will make future tests more reliable.