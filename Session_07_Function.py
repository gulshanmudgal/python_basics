def hello_func(greeting, name="You"):
    return "{}, {}!".format(greeting, name)

result = hello_func("Hi", "Alice")
print(result)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Science", "Math", name = "Alice", grade="A", age=20)
course = ["Science", "Math"]
info = {"name": "Alice", "grade": "A", "age": 20}

student_info(course, info) # This will treat course and info as single arguments
student_info(*course, **info) # This will unpack the lists and dictionaries correctly

months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_lepap_year(year):
    """Return True if year is a leap year, else False."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_months(year, month):
    """Return number of days in that month in that year."""

    if not 1<= month <= 12:
        return "Invalid Month"
    
    if month == 2 and is_lepap_year(year):
        return 29
    
    return months_days[month]

print(days_in_months(2020, 2))  # Leap year
print(days_in_months(2019, 2))  # Non-leap year