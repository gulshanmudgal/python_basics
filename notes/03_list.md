# 03 Lists, Tuples, and Sets Notes

## Lists
Lists are mutable collections of items.

### Creating and Accessing
- `courses = ["History", "Maths", "Physics", "Compute Science"]`
- `len(courses)`: Get length
- `courses[0]`: First item
- `courses[-1]`: Last item

### Slicing
- `courses[0:2]`: Items 0 to 1
- `courses[2:]`: From index 2 to end
- `courses[:2]`: From start to index 1

### Modifying Lists
- `courses.append("Electronics")`: Add to end
- `courses.insert(0, "Mechanics")`: Insert at index
- `courses.extend(another_list)`: Add items individually (vs. append which adds the list as one item)
- `courses.remove("item")`: Remove by value
- `courses.pop()`: Remove last item

### Sorting
- `nums.sort()`: Sort in place (ascending)
- `nums.sort(reverse=True)`: Sort descending
- `sorted(courses)`: Return sorted copy without changing original

### Math Functions (for numeric lists)
- `min(nums)`, `max(nums)`, `sum(nums)`

### Searching
- `courses.index("Maths")`: Get index (raises error if not found)
- `"item" in courses`: Check if exists

### Iteration
- `for course in courses: print(course)`
- `for index, course in enumerate(courses): print(index, course)`
- `for index, course in enumerate(courses, start=1): print(index, course)`

### List Comprehension
- `nums = [num * 2 for num in nums]`: Create new list with transformations

### Join and Split
- `", ".join(courses)`: Join list into string
- `courses_str.split(", ")`: Split string into list

## Tuples
Tuples are immutable collections.

- `new_courses = ("History", "Maths", "Physics", "Compute Science")`
- Cannot modify: `new_courses[0] = "Mechanics"` → Error

## Sets
Sets are unordered, unchangeable, unindexed collections. No duplicates.

- `cs_courses_set = {"History", "Maths", "Physics", "Compute Science"}`
- `intersection(other_set)`: Common items
- `difference(other_set)`: Items in first but not second
- `union(other_set)`: All unique items

## Empty Collections
- List: `[]` or `list()`
- Tuple: `()` or `tuple()`
- Set: `set()` (not `{}` which is dict)

## Key Points
- Lists are mutable; tuples are immutable.
- Sets automatically remove duplicates and are unordered.
- Use list comprehension for concise transformations.