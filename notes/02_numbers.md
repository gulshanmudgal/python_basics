# 02 Numbers Notes

## Arithmetic Operators
- Addition: `3 + 2` → 5
- Subtraction: `3 - 2` → 1
- Multiplication: `3 * 2` → 6
- Division: `3 / 2` → 1.5
- Floor Division: `3 // 2` → 1 (integer division)
- Modulus: `3 % 2` → 1 (remainder)
- Exponentiation: `3 ** 2` → 9

## Augmented Assignments
- `num += 3` → `num = num + 3`
- `num *= 6` → `num = num * 6`
- Similar for `-=`, `/=`, `//=`, `%=`, `**=`

## Built-in Functions
- `abs(x)`: Absolute value, e.g., `abs(-3)` → 3
- `round(x)`: Round to nearest integer, e.g., `round(3.75)` → 4
- `round(x, n)`: Round to n decimal places, e.g., `round(3.75, 1)` → 3.8

## Comparison Operators
- Equal: `==`, e.g., `3 == 2` → False
- Not Equal: `!=`, e.g., `3 != 2` → True
- Greater Than: `>`, e.g., `3 > 2` → True
- Less Than: `<`, e.g., `3 < 2` → False
- Greater Than or Equal: `>=`, e.g., `3 >= 2` → True
- Less Than or Equal: `<=`, e.g., `3 <= 2` → False

## Type Casting
- `int(x)`: Convert to integer, e.g., `int(3.75)` → 3
- `float(x)`: Convert to float, e.g., `float(8)` → 8.0
- Convert strings to numbers: `int('100')` → 100

## Key Points
- Be careful with division: `/` gives float, `//` gives int.
- String concatenation vs. numeric addition: `'100' + '200'` → '100200', but `int('100') + int('200')` → 300.