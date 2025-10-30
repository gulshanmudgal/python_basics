# 07 Functions Notes

## Defining Functions
```python
def function_name(parameters):
    # code
    return value
```

## Parameters and Default Values
- `def hello_func(greeting, name="You"):`
- Default values make parameters optional.

## *args and **kwargs
- `*args`: Variable number of positional arguments (tuple)
- `**kwargs`: Variable number of keyword arguments (dict)

```python
def student_info(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # dict
```

## Unpacking Arguments
- `*list`: Unpack list as positional args
- `**dict`: Unpack dict as keyword args

```python
student_info(*course, **info)  # Unpacks correctly
```

## Docstrings
- Document functions: `"""Description."""`

## Example: Days in Month
```python
def is_leap_year(year):
    """Return True if year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap_year(year):
        return 29
    return months_days[month]
```

## Key Points
- Functions help organize code.
- Use `*args` for flexible positional args, `**kwargs` for keyword args.
- Unpacking with `*` and `**` passes elements individually.