# 01 Strings Notes

## String Basics
- Strings are sequences of characters.
- Can be defined using single quotes ('), double quotes ("), or triple quotes (""" or ''') for multiline.
- Example: `message = "Hello, World"`

## Indexing and Slicing
- Strings are indexed starting from 0.
- Access individual characters: `message[0]` → 'H'
- Slicing: `message[0:5]` → 'Hello' (start inclusive, end exclusive)
- `message[:5]` → first 5 characters
- `message[7:]` → from index 7 to end

## Handling Quotes
- Use single quotes for strings with double quotes inside: `'Gullu"s World'`
- Use double quotes for strings with single quotes inside: `"Gullu's World"`
- Escape quotes: `'Gullu\'s World'` or `"Gullu\"s World"`

## Multiline Strings
- Use triple quotes for multiline strings.
- Example:
  ```
  multilineMessage = """This is a multi line message
  this will appear on multiple lines."""
  ```

## String Concatenation
- Use `+` operator: `greeting + " " + name`

## String Formatting
- Old way: `"{}, {}, Welcome!".format(greeting, name)`
- Modern way (f-strings): `f"{greeting}, {name.upper()}, Welcome!"`

## String Methods
- `lower()`: Convert to lowercase
- `dir(str)`: List all available methods for strings
- `help(str.lower)`: Get help on a specific method

## Key Points
- Strings are immutable in Python.
- Use `dir()` and `help()` to explore string methods.
