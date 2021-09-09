## Exception Handling



```python
while True print('Hello')
```

<!-- #region -->
```python
File "/tmp/ipykernel_32/979740009.py", line 1
    while True print('Hello')
               ^
SyntaxError: invalid syntax
```
<!-- #endregion -->

```python
10 * (1/0)
```

<!-- #region -->
```python
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
/tmp/ipykernel_46/734848216.py in <module>
----> 1 10 * (1/0)

ZeroDivisionError: division by zero
```
<!-- #endregion -->

```python
4 + spam*3
```

<!-- #region -->
```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_46/2481180859.py in <module>
----> 1 4 + spam*3

NameError: name 'spam' is not defined
```
<!-- #endregion -->

```python
'2' + 2
```

<!-- #region -->
```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_46/209420021.py in <module>
----> 1 '2' + 2

TypeError: can only concatenate str (not "int") to str
```
<!-- #endregion -->

There is a list of [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) available in the python docs [2].


### Handling Exceptions

```python
go = True
while go:
    try:
        x = int(input("Please enter a number: "))
        go = False
    except ValueError: 
        print("Oops! Tat was no valid number. Try again...")
```

<!-- #region -->
The code above implies that only `ValueErrors` are handled whilst the rest are allowed to bubble up. Which effectively implies another except statement as follows:
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```
<!-- #endregion -->

You can also create your own exception classes:

```python
# Base Class Example 1
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')
```

```python
# Base Class Example 2
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print('B')
    except D:
        print('D')
    except C:
        print('C')
```

**What is going on?**

When an exception is thrown, python goes the first path that matches the class instance type. In the examples above, `class C` and `class D` are derived classses of `class B`, which is consequently referred to as the base class. In `example 1`, wen a `class C` hexception is raised, `except D` and `except C`, but not `except B` is checked. Python checks `except D` sees that `C` class does match, i.e. is same or that is a base class, so it moves on. It then gets to `except C` which is the same class and so follows that path.

In `example 2`, `class C` would go down the first `except B` path as `class B` is the a base class to `class C`, eventhough a better match is present further down. 

This means you need to be very mindful of the order and base-derived class relationships present in your custom exceptions.

```python
import sys

try: 
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS Error: {0}".format(err))
except ValueError:
    print("Coulb not convert data to an integer.")
except:
    print("Unexpcted error:", system.exc_info()[0])
    raise
```

<!-- #region -->
```python
OS Error: [Errno 2] No such file or directory: 'myfile.txt'
```
<!-- #endregion -->

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else: 
        # runs statements when none of except scenarios match, important to have.
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

<!-- #region -->
```python
cannot open -f
/root/.local/share/jupyter/runtime/kernel-c6d7de2f-4fdb-4a53-a4dc-fc4df05f9646.json has 12 lines
```
<!-- #endregion -->

```python
try: 
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    
    x, y = inst.args
    print('x =', x)
    print('y =', y)
```

<!-- #region -->
```python
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
<!-- #endregion -->

```python
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling runt-time error;', err)

```

<!-- #region -->
```python
Handling runt-time error; division by zero
```
<!-- #endregion -->

### Raising Exceptions

```python
raise NameError('HiThere')
```

<!-- #region -->
```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_70/2916444848.py in <module>
----> 1 raise NameError('HiThere')

NameError: HiThere
```
<!-- #endregion -->

```python
raise ValueError
```

<!-- #region -->
```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/tmp/ipykernel_70/4096975414.py in <module>
----> 1 raise ValueError

ValueError: 
```
<!-- #endregion -->

```python
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise  # rethrows the exception into oblivion!
```

<!-- #region -->
```python
An exception flew by!
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_70/1719713102.py in <module>
      1 try:
----> 2     raise NameError('HiThere')
      3 except NameError:
      4     print('An exception flew by!')
      5     raise  # rethrows the exception into oblivion!

NameError: HiThere
```
<!-- #endregion -->

```python
def func():
    raise IOError
    
try: 
    func()
except IOError as exc:
    raise RuntimeError('Faised to open database') from exc
```

<!-- #region -->
```python
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
/tmp/ipykernel_70/1798935421.py in <module>
      4 try:
----> 5     func()
      6 except IOError as exc:

/tmp/ipykernel_70/1798935421.py in func()
      1 def func():
----> 2     raise IOError
      3 

OSError: 

The above exception was the direct cause of the following exception:

RuntimeError                              Traceback (most recent call last)
/tmp/ipykernel_70/1798935421.py in <module>
      5     func()
      6 except IOError as exc:
----> 7     raise RuntimeError('Falsed to open database') from exc

RuntimeError: Falsed to open database
```
<!-- #endregion -->

note that the `from exc` is a default feature, that is if an exception is thrown whilst an exception is being handled, the initial exception is preserved:

```python
def func():
    raise IOError
    
try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database')
```

<!-- #region -->
```python
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
/tmp/ipykernel_70/551355716.py in <module>
      4 try:
----> 5     func()
      6 except IOError as exc:

/tmp/ipykernel_70/551355716.py in func()
      1 def func():
----> 2     raise IOError
      3 

OSError: 

During handling of the above exception, another exception occurred:

RuntimeError                              Traceback (most recent call last)
/tmp/ipykernel_70/551355716.py in <module>
      5     func()
      6 except IOError as exc:
----> 7     raise RuntimeError('Failed to open database')

RuntimeError: Failed to open database
```
<!-- #endregion -->

```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None # OSError was not preserved
```

<!-- #region -->
```python
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
/tmp/ipykernel_70/669350098.py in <module>
      2     open('database.sqlite')
      3 except OSError:
----> 4     raise RuntimeError m
RuntimeError: 
```
<!-- #endregion -->

### User-defined Exceptions

```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for error in the input.
    
    Attributes: 
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class TRansitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of mwhy the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```

### Defining Clean-up Actions

```python
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```

<!-- #region -->
```python
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
/tmp/ipykernel_70/163421838.py in <module>
      1 try:
----> 2     raise KeyboardInterrupt
      3 finally:
      4     print('Goodbye, world!')

KeyboardInterrupt: 
```
<!-- #endregion -->

```python
def bool_return():
    try:
        return True
    finally:
        return False
    
bool_return()
```

```python
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', result)
    finally:
        print('executing finally clause')
```

```python
divide(2,0)
```

```python
divide(2,0)
```

```python
divide('2', '1')
```

some objects have predefined clean up actions

```python
for line in open('myfile.txt'):
    print(line, end=' ')
    
# this is brain-dead code, effectively leaving the file open
```

the following method has a `finally` statement built in.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end=" ")
```

### References

1. [Errors and Exceptions -- Python Documentation](https://docs.python.org/3/tutorial/errors.html)

2. [Built-in Exceptions -- Python Documentation](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
