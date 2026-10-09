# Day 8: Function Design and Caesar Cipher

## Learned

- Positional arguments depend on order; keyword arguments communicate intent.
- Functions can transform data and return the result to their caller.
- A Caesar cipher uses an alphabet index and modular wrapping.
- Encoding and decoding are the same operation with opposite shifts.

## Topics in plain language

- **Argument order:** whether values are matched by their position in a function call.
- **Keyword argument:** a value passed by naming the parameter, such as `shift=3`.
- **Index:** a number representing a character's position in a string.
- **Encoding:** changing readable information into another representation.
- **Decoding:** changing an encoded representation back toward readable information.
- **Modulo wrapping:** moving past the last position and continuing from the first.

## Practice record

Built three iterations of Caesar Cipher and practiced functions with inputs.

## Small example

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

def shift_letter(letter, shift):
	old_index = alphabet.index(letter)
	new_index = (old_index + shift) % len(alphabet)
	return alphabet[new_index]


print(shift_letter("z", 1))
```

Modulo wraps the index back to the beginning after it reaches the end.

## Technical Python practice

Practiced string indexing, `str.index()`, modular arithmetic, and returning a transformed character from a function.

```python
alphabet = "abc"
position = alphabet.index("c")
shifted_position = (position + 1) % len(alphabet)
print(alphabet[shifted_position])
```

## Next review

Add tests for shifts larger than the alphabet and for punctuation and spaces.

## What went wrong or remains unclear

Cipher indexes can go outside the alphabet unless modulo is used. Non-letter characters also need an explicit policy instead of accidental transformation.