# 06 Loops Notes

## For Loops
Iterate over sequences like lists.

```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
```

## Continue Statement
Skip the rest of the loop iteration and continue to the next.

```python
for num in nums:
    if num == 3:
        print("Skipping 3")
        continue
    print(num)
```

## Range Function
Generate sequences of numbers.

- `range(10)`: 0 to 9
- `range(1, 11)`: 1 to 10

```python
for i in range(10):
    print(i)  # 0 to 9

for i in range(1, 11):
    print(i)  # 1 to 10
```

## Key Points
- `for` loops are used for definite iteration.
- `continue` skips to the next iteration.
- `range(start, stop)` generates from start to stop-1.