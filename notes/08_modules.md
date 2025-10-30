# 08 Modules Notes

## Importing Modules
- `import module_name`: Import the entire module
- Access with `module_name.function()` or `module_name.variable`

## Import Variations
There are several ways to import modules and their contents:

### Standard Import
- `import module_name`
- Access items with `module_name.item`

Example:
```python
import math
print(math.sqrt(16))  # 4.0
```

### From Import (Specific Items)
- `from module import item1, item2`
- Import specific functions/variables directly

Example:
```python
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.14159...
```

### Import with Alias
- `import module as alias`
- Shorten long module names

Example:
```python
import numpy as np
arr = np.array([1, 2, 3])
```

### From Import with Alias
- `from module import item as alias`

Example:
```python
from math import sqrt as square_root
print(square_root(16))  # 4.0
```

### Import All
- `from module import *`
- Import everything (not recommended, pollutes namespace)

Example:
```python
from math import *
print(sin(pi/2))  # 1.0
```

### Importing from Packages
- `from package import module`
- `from package.module import function`

Example:
```python
from os import path
print(path.join('folder', 'file.txt'))
```

### Relative Imports (in packages)
- `from . import module` (current package)
- `from .. import module` (parent package)

Example:
```python
# In subpackage/module.py
from . import helper
from ..utils import common_func
```

### Conditional Imports
- Import based on conditions (e.g., platform)

Example:
```python
try:
    import json
except ImportError:
    import simplejson as json
```

### Importing Multiple Modules
- `import module1, module2`

Example:
```python
import os, sys
print(os.getcwd())
print(sys.version)
```

Example:
```python
import mymodule
index = mymodule.find_index(course, "Math")
```

## Creating Modules
A module is a Python file (.py) that can be imported.

- Create a file like `mymodule.py`
- Define functions, variables, classes
- When imported, code at module level runs (e.g., print statements)

Example `mymodule.py`:
```python
print('Imported My Module')  # Runs on import

test = 'This is a test string'

def find_index(to_search, target):
    """Find index of target in to_search."""
    for i in range(len(to_search)):
        if to_search[i] == target:
            return i
    return -1
```

## __name__ Variable
The `__name__` attribute helps determine how a module is being used.

- When a Python file is run directly: `__name__ == "__main__"`
- When imported as a module: `__name__ == "module_name"`

### Use Case: Running Code Only When Executed Directly
Use `if __name__ == "__main__":` to prevent code from running when imported.

Example in `mymodule.py`:
```python
def greet(name):
    return f"Hello, {name}!"

# This runs only when mymodule.py is executed directly
if __name__ == "__main__":
    print(greet("World"))  # Output: Hello, World!
    print("This is a test run.")
```

If you run `python mymodule.py`, it prints the messages. If imported (`import mymodule`), the print statements don't execute.

### Use Case: Testing Functions in Modules
Add test code that runs only when the module is the main script.

Example:
```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    # Test the function
    result = add(2, 3)
    print(f"Test: 2 + 3 = {result}")  # Test: 2 + 3 = 5
    assert result == 5, "Test failed!"
    print("All tests passed.")
```

### Use Case: Command-Line Scripts
Modules can act as both libraries and scripts.

Example `calculator.py`:
```python
def calculate(a, b, op):
    if op == '+':
        return a + b
    # ... other operations

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <a> <op> <b>")
    else:
        a, op, b = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
        result = calculate(a, b, op)
        print(f"{a} {op} {b} = {result}")
```

Run as script: `python calculator.py 5 + 3` → `5 + 3 = 8`

Import as module: `from calculator import calculate` (no output)

### Key Points
- `__name__` allows modules to be both importable and executable.
- Essential for writing reusable code with built-in tests.
- Common in Python scripts and libraries.

## Packages
Packages are directories that contain multiple modules, allowing for better organization of code.

### Creating Packages
- A package is a directory containing an `__init__.py` file (can be empty).
- Modules within the package can import each other.

Example package structure:
```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

### __init__.py File
- Makes Python treat the directory as a package.
- Can be empty or contain initialization code.
- Runs when the package is imported.

Example `__init__.py`:
```python
# Can be empty
# Or initialize package-level variables
__version__ = "1.0.0"
```

### Importing from Packages
- `from package import module`
- `from package.module import function`
- `import package.module`

Example:
```python
# Assuming mypackage/module1.py has def func1():
from mypackage import module1
module1.func1()

# Or
from mypackage.module1 import func1
func1()
```

### Package with Subpackages
Packages can contain subpackages.

Structure:
```
project/
├── __init__.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── main.py
```

Importing:
```python
from project.utils import helpers
helpers.some_function()
```

### Use Case: Organizing Large Projects
Group related modules into packages for maintainability.

Example: Web app structure
```
webapp/
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
├── views/
│   ├── __init__.py
│   └── home.py
└── utils/
    ├── __init__.py
    └── database.py
```

### Use Case: Sharing Common Code
Use packages to share utilities across modules.

Example in `utils/__init__.py`:
```python
from .database import connect_db
from .helpers import format_date
```

Then import: `from utils import connect_db, format_date`

### Namespace Packages (Python 3.3+)
- No `__init__.py` needed.
- Useful for distributing packages across directories.

### Key Points
- `__init__.py` is required for packages in Python < 3.3.
- Packages help avoid name conflicts and organize code.
- Use relative imports within packages for better portability.



## Gotchas
Common pitfalls when working with modules and packages.

### Circular Imports
When two modules try to import each other, causing an ImportError.

Example:
```python
# module_a.py
import module_b

def func_a():
    module_b.func_b()

# module_b.py
import module_a  # This causes circular import error

def func_b():
    module_a.func_a()
```

**Solution**: Restructure code to avoid mutual dependencies. Use local imports or move shared code to a third module.

### Import Order Matters
Imports execute top to bottom. Side effects can cause issues if modules depend on each other.

Example:
```python
# config.py
DATABASE_URL = "sqlite:///:memory:"

# app.py
import config  # Must import config before using it
print(config.DATABASE_URL)
```

**Issue**: If config is imported after it's used, NameError occurs.

### Module Caching
Modules are loaded once per session. Changes aren't reflected without reload.

Example:
```python
import mymodule
# Edit mymodule.py
# Still uses cached version
```

**Solution**: Use `importlib.reload()` for development:
```python
import importlib
import mymodule
# Edit mymodule.py
importlib.reload(mymodule)
```

### Relative Imports Issues
Relative imports (`from . import`) only work inside packages and when run as part of a package.

Example:
```python
# In package/submodule.py
from . import helper  # Works when imported as package.submodule
# But fails if run directly: python submodule.py
```

**Solution**: Use absolute imports for scripts that might be run standalone.

### sys.path Problems
Python searches `sys.path` for modules. Custom modules not in these paths cause ImportError.

Example:
```python
import sys
print(sys.path)  # Shows search paths
```

**Solution**: Add custom paths:
```python
import sys
sys.path.append('/path/to/my/modules')
import mymodule
```

Or use PYTHONPATH environment variable.

### Name Conflicts
Naming modules the same as built-ins or standard library modules causes shadowing.

Example:
```python
# os.py (bad name)
def my_func():
    pass

# main.py
import os  # Imports your os.py, not the standard library
os.path.join(...)  # AttributeError!
```

**Solution**: Avoid names like `os.py`, `sys.py`, `math.py`. Use unique names.

## Best Practices
Guidelines for effective module and package management.

### Use `if __name__ == "__main__"` for Scripts
Separate executable code from importable code.

Example:
```python
def main():
    # Script logic here
    pass

if __name__ == "__main__":
    main()
```

**Benefit**: Module can be imported without running the script.

### Prefer Absolute Imports
Use full paths from project root for clarity and reliability.

Example:
```python
# Good
from myproject.utils.helpers import format_date

# Avoid
from ..utils.helpers import format_date  # Relative, fragile
```

### Keep Modules Focused
Each module should have a single responsibility.

Example: Instead of one large `utils.py`, use:
```
utils/
├── __init__.py
├── string_utils.py
├── file_utils.py
└── math_utils.py
```

### Use Packages for Organization
Group related modules into packages.

Example structure:
```
myapp/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── models.py
│   └── views.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── tests/
    ├── __init__.py
    └── test_models.py
```

### Handle Import Errors Gracefully
Use try/except for optional dependencies.

Example:
```python
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pd = None
```

### Document Your Modules
Use docstrings and comments.

Example:
```python
"""
Math utilities module.

This module provides mathematical helper functions.
"""

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)
```

### Version Your Packages
Include version info in `__init__.py`.

Example:
```python
# mypackage/__init__.py
__version__ = "1.2.3"
__author__ = "Your Name"
```

### Test Your Imports
Ensure modules can be imported without errors.

Example: Run `python -c "import mymodule"` to test.