# 05 Conditionals Notes

## Comparison Operators
- Equal: `==`
- Not Equal: `!=`
- Greater Than: `>`
- Less Than: `<`
- Greater Than or Equal: `>=`
- Less Than or Equal: `<=`
- Object Identity: `is` (checks if same object in memory)
- Object Non-Identity: `is not`

## If, Elif, Else
```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```
- Example:
  ```python
  if language == "Python":
      print("Python")
  elif language == "Java":
      print("Java")
  else:
      print("Not Matched")
  ```

## Logical Operators
- `and`: Both conditions must be true
- `or`: At least one condition must be true
- `not`: Negates the condition

Examples:
- `if user == "Admin" and logged_in:`
- `if user == "Admin" or logged_in:`
- `if not logged_in:`

## Identity vs Equality
- `==`: Checks if values are equal
- `is`: Checks if same object in memory
- Example: `a = [1,2,3]; b = [1,2,3]; a == b` → True, `a is b` → False

## Falsy Values
Values that evaluate to False in conditions:
- `False`
- `None`
- `0`
- `0.0`
- Empty sequences: `''`, `()`, `[]`, `{}`
- Empty mappings: `{}`

Example:
```python
condition = {}
if condition:
    print("True")
else:
    print("False")  # This will print
```

## Key Points
- Use `is` for None checks: `if x is None:`
- Conditions can be chained with logical operators.
- Indentation is crucial in Python.