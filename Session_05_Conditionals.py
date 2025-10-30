# Comparison Operators
# Equal:                     ==
# Not Equal:                 !=
# Greater than:              >
# Less than:                 <
# Greater than or equal to:  >=
# Less than or equal to:     <=
# Object Identity:           is
# Object Non-Identity:       is not

# If, Elif, Else Examples
language = "Java"

if language == "Python":
    print("The language is Python")
elif language == "Java":
    print("The language is Java")
elif language == "JavaScript":
    print("The language is JavaScript")
else:
    print("Not Matched")

# Logical Operators Examples
user = "Admin"
logged_in = False

# AND example
if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# OR example
if user == "Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# NOT example
if not logged_in:
    print("Please Log In")
else:
    print("Welcome")


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # Memory address of a
print(id(b))  # Memory address of b
print(a == b)  # True, because values are the same
print(a is b)  # False, because they are different objects in memory

# Falsey Values in Python
# False
# None
# 0
# 0.0
# any empty sequence or collection: '', (), [], {}
# any empty mapping: {}

condition = {}

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
