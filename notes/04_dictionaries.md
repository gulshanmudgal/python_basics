# 04 Dictionaries Notes

## Creating Dictionaries
Dictionaries are key-value pairs, unordered and mutable.

- `student = {'Name': 'John', 'Age': 20}`

## Accessing Values
- `student['key']`: Raises KeyError if key doesn't exist
- `student.get('key')`: Returns None if key doesn't exist
- `student.get('key', 'default')`: Returns default if key doesn't exist

## Adding and Updating
- `student['Phone'] = '123-456-7890'`: Add new key-value
- `student['Age'] = 21`: Update existing
- `student.update({'Name': 'Jane', 'Email': 'john@doe.com'})`: Update multiple

## Deleting
- `del student['Email']`: Delete key-value pair
- `age = student.pop('Age')`: Remove and return value

## Other Operations
- `len(student)`: Number of key-value pairs
- `student.keys()`: All keys
- `student.values()`: All values
- `student.items()`: All key-value pairs as tuples

## Iteration
- `for key in student: print(key)`
- `for key, value in student.items(): print(f"{key}: {value}")`

## Checking Existence
- `'key' in student`: Check if key exists
- `'value' in student.values()`: Check if value exists

## Key Points
- Dictionaries are unordered (in Python < 3.7; ordered in 3.7+).
- Use `get()` to avoid KeyError.
- Keys must be immutable (strings, numbers, tuples).