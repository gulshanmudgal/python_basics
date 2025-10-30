# Printing welcome message
message = "Hello, World"
print(message)
print(message[0])
print(message[0:5]) # First Index is start index, second index is ending index, but, last index wouldn't be considered for printing
print(message[:5])
print(message[7:])

messageWithSingleQuote = "Gullu's World"
print(messageWithSingleQuote)

messageWithDoubleQuote = 'Gullu"s World'
print(messageWithDoubleQuote)

# Better Approach for handling single and double quotes
messageWithSingleQuote = 'Gullu\'s World'
print(messageWithSingleQuote)

messageWithDoubleQuote = "Gullu\"s World"
print(messageWithDoubleQuote)

multilineMessage = """This is a multi line message
this will appear on multile lines."""

print(multilineMessage)

print(multilineMessage.lower())


# String Concatenation
greeting = "Hello"
name = "Gullu"
print(greeting + " " + name)

# String Formatting 2 - Better way
message = "{}, {}, Welcome!".format(greeting, name)
print(message)

# String Formatting 3 - Best way
message = f"{greeting}, {name.upper()}, Welcome!"
print(message)

print(dir(name)) # To get all the methods available for string
print(help(str.lower)) # To get help on specific method