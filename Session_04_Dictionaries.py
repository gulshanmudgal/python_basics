student = {'Name': 'John', 'Age': 20}

print(student)
# print(student['Phone']) # This will raise a KeyError since 'Phone' is not a key in the dictionary
print(student.get('Phone')) # This will return None instead of raising an error
print(student.get('Phone', 'Not Found')) # This will return 'Not Found' if 'Phone' is not a key in the dictionary

student['Phone'] = '123-456-7890' # Adding a new key-value pair
print(student)

# Updating an existing key-value pair
student['Age'] = 21
print(student)

student.update({'Name': 'Jane', 'Email': 'john@doe.com'}) # Updating multiple key-value pairs
print(student)

# Deleting a key-value pair
del student['Email']
print(student)

age = student.pop('Age') # Removing a key-value pair and getting its value
print(f"Removed Age: {age}")
print(student)
print(len(student)) # Getting the number of key-value pairs in the dictionary

# Iterating through the dictionary
print(student.keys()) # Getting all keys
print(student.values()) # Getting all values
print(student.items()) # Getting all key-value pairs

for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
if 'Name' in student:
    print("Name exists in the dictionary")
else:
    print("Name does not exist in the dictionary")

# checking if a value exists in the dictionary
if 'John' in student.values():
    print("John exists in the dictionary")
else:
    print("John does not exist in the dictionary")