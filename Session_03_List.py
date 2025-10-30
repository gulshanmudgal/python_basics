# List is a collection of items
courses = ["History", "Maths", "Physics", "Compute Science"]
print(courses) #To print the complete 
print(len(courses)) #To print the length of the list
print(courses[0]) #To print the first item of the list
print(courses[-1]) #To print the last item of the list
print()

# To print the items of the list in a range
print(courses) #To print the complete list
print(courses[0:2]) #To print the items of the list in a range
print(courses[0:6]) #To print the items of the list in a range even if the range is more than the length of the list
print(courses[2:]) #To print the items of the list in a range from the 2nd item to the end
print(courses[:2]) #To print the items of the list in a range from the start to the 2nd item
print()

# To Handle append and insert
# append will add the item at the end of the list
# insert will add the item at the given indexs
courses.append("Electronics") # by default the append function will append the item in the end
courses.insert(0, "Mechanics") # this will insert the item at given index

# To Diffrentiate between append and extend with another list
# append will add the list as a single item
# extend will add the items of the list individually
courses_2 = ["Arts", "Woke Arts"]

# courses.append(courses_2) # basically the complete list 2 is appeded into the courses as a list item, being the List of List 
print(courses)
print(courses_2)

courses.extend(courses_2) # This ensures that items are added individually to the courses list
print(courses)
print(courses_2)


# To remove the items from the list
# There are two ways of removing the items from List
courses.remove("Mechanics")
print(courses)

courses.pop() # This will remove that item from back
print(courses)
print()

# To sort the list
nums = [1, 9, 8, 4, 5, 6, 7]
nums.sort() # This will sort the list in ascending order
print(nums)

nums.sort(reverse=True) # This will sort the list in descending order
print(nums)
print()

print(sorted(courses)) # This will sort the list in ascending order but will not change the original list

# Math Functions for numeric list
print(min(nums)) # This will print the minimum value of the list
print(max(nums)) # This will print the maximum value of the list
print(sum(nums)) # This will print the sum of the list

# Find the index of an item in the list
print(courses.index("Maths")) # This will print the index of the item in the list, if the item is not found it will give an value error
print("Art" in courses) # This will print True if the item is found in the list, otherwise it will print False


# For loop to iterate through the list
for course in courses:
    print(course) # This will print each item of the list

for index, course in enumerate(courses):
    print(index, course) # This will print the index and the item of the list

for index, course in enumerate(courses, start = 1):
    print(index, course) # This will print the index and the item of the list

print()

# List Comprehension
# This is a way to create a new list from an existing list
# This will create a new list with the items of the existing list
# This will create a new list with the items of the existing list multiplied by 2
nums = [1, 2, 3, 4, 5]
nums = [num * 2 for num in nums] # This will create a new list with the items of the existing list multiplied by 2
print(nums) # This will print the new list
# This will create a new list with the items of the existing list multiplied by 2 and only even numbers

# 
courses_str = ", ".join(courses) # This will join the items of the list with a comma and space
print(courses_str) # This will print the new list
new_list = courses_str.split(", ") # This will split the string into a list
print(new_list) # This will print the new list

#Tuples
# Tuples are immutable
# Tuples are used to store multiple items in a single variable
new_courses = ("History", "Maths", "Physics", "Compute Science")
new_courses2 = new_courses
print(new_courses) #To print the complete list
print(new_courses2) #To print the first item of the list

# new_courses2[0] = "Mechanics" # This will give an error because tuples are immutable
# print(new_courses) #To print the complete list

#Sets
# Sets are used to store multiple items in a single variable
# Sets are unordered, meaning that the items have no index
# Sets are unchangeable, meaning that we cannot change the items in a set
# Sets are unindexed, meaning that we cannot access the items in a set
# Sets are written with curly brackets

cs_courses_set = {"History", "Maths", "Physics", "Compute Science"}
arts_courses_set = {"History", "Maths", "Arts", "Woke Arts"}
print(cs_courses_set) #To print the complete set
print(arts_courses_set) #To print the complete set

print(cs_courses_set.intersection(arts_courses_set)) # This will print the common items in both sets
print(cs_courses_set.difference(arts_courses_set)) # This will print the items that are in cs_courses_set but not in arts_courses_set
print(cs_courses_set.union(arts_courses_set)) # This will print all the items in both sets, but will not print the duplicate items

# empty list
empty_list = []
empty_list = list()

# empty tuple
empty_tuple = ()
empty_tuple = tuple()

# empty set
empty_set = {} # This will create an empty dictionary
empty_set = set() # This will create an empty set