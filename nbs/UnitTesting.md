---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

### Unit Testing


Notes on Unit Testing in Python

```python
import pyExamples.calc as calc
```

The `calc` module offers a few math functions which we'll test to see it they work.

```python
calc.add(4,5)
```

within `src/test_calc.py` we have the unit testing module, which some code to test the first function in `calc`

<!-- #raw -->
import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
        
if __name__ == "__main__":
    unittest.main()
<!-- #endraw -->

<!-- #raw -->
Notice `line 10` which calls unittest.main() when the module is called directly like below.
<!-- #endraw -->

```python
! python ./src/test_calc.py
```

There are 4 tests inside the `test_calc.py` file, their successful run is represented as a dot `.` in the terminal.


this is to prevent having to write the below which makes automating testing awkward:

<!-- #raw -->
! python -m unittest ./src/test_calc.py
<!-- #endraw -->

<!-- #raw -->
[...]

    def test_divide(self):
    
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
       
        self.assertRaises(ZeroDivisionError, calc.divide, 10, 0)
        
[...]
<!-- #endraw -->

You can have multiple assertions under the same test, although it may be harder to tell which of those tests failed. The example above also shows how you can use the `assertRaises` function to see if the correct error is thrown.


You can also use a Context Manager to assert this test:

<!-- #raw -->
[...] 

    def test_divide(self):
    
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10,0)
    
[...]
<!-- #endraw -->

```python
#TODO
import pyExamples.test_calc as test_calc
```

Unittest offers some `@classmethod` which allows some code to be run before and after all the tests. A good reference to classmethods is [[so-class-static-method](https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner)].

<!-- #raw -->
class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs before all tests, useful for setup of stateful elements."""
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        """Runs after all tests, useful to post cleanup of stateful elements"""
        print('teardownClass')

[...] 
<!-- #endraw -->

`[?]` How do you mock with Unit Tests?

see [[shafer-unittesting](https://youtu.be/6tNS--WetLI?t=1738)]

```python
from unittest.mock import patch
```
