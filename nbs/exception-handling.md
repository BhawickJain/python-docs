
## Exception Handling


+++

#### Types of Errors

```{code-cell} ipython3
while True print('Hello')
```

```python
File "/tmp/ipykernel_32/979740009.py", line 1
    while True print('Hello')
               ^
SyntaxError: invalid syntax
```

```{code-cell} ipython3
10 * (1/0)
```

```python
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
/tmp/ipykernel_46/734848216.py in <module>
----> 1 10 * (1/0)

ZeroDivisionError: division by zero
```

```{code-cell} ipython3
4 + spam*3
```

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_46/2481180859.py in <module>
----> 1 4 + spam*3

NameError: name 'spam' is not defined
```

```{code-cell} ipython3
'2' + 2
```

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_46/209420021.py in <module>
----> 1 '2' + 2

TypeError: can only concatenate str (not "int") to str
```

+++

There is a list of [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) available in the python docs [2].

+++

#### Handling Exceptions

```{code-cell} ipython3
go = True
while go:
    try:
        x = int(input("Please enter a number: "))
        go = False
    except ValueError: 
        print("Oops! Tat was no valid number. Try again...")
```

The code above implies that only `ValueErrors` are handled whilst the rest are allowed to bubble up. Which effectively implies another except statement as follows:
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

+++

You can also create your own exception classes:

```{code-cell} ipython3
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

```{code-cell} ipython3
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

```{code-cell} ipython3
import sys

try: 
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# except FileNotFoundError as err:
#     print(f"File not found: {err}")
except OSError as err:
    print("OS Error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpcted error:", system.exc_info()[0])
    raise
```

Interesting that `FileNotFoundError` must be a derived class of `OSError`.

`[?]` Is the `FileNotFoundError` a derived class of the more generic `OSError`?  
`[?]` Is it better to use the more generic `OSError` in the code example below?

+++

```python
OS Error: [Errno 2] No such file or directory: 'myfile.txt'
```

```{code-cell} ipython3
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

```python
cannot open -f
/root/.local/share/jupyter/runtime/kernel-c6d7de2f-4fdb-4a53-a4dc-fc4df05f9646.json has 12 lines
```

```{code-cell} ipython3
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

```python
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

```{code-cell} ipython3
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling runt-time error;', err)
```

```python
Handling runt-time error; division by zero
```

+++

### Raising Exceptions

```{code-cell} ipython3
raise NameError('HiThere')
```

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_70/2916444848.py in <module>
----> 1 raise NameError('HiThere')

NameError: HiThere
```

```{code-cell} ipython3
raise ValueError
```

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/tmp/ipykernel_70/4096975414.py in <module>
----> 1 raise ValueError

ValueError: 
```

```{code-cell} ipython3
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise  # rethrows the exception into oblivion!
```

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

```{code-cell} ipython3
def func():
    raise IOError
    
try: 
    func()
except IOError as exc:
    raise RuntimeError('Faised to open database') from exc
```

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

+++

note that the `from exc` is a default feature, that is if an exception is thrown whilst an exception is being handled, the initial exception is preserved:

```{code-cell} ipython3
def func():
    raise IOError
    
try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database')
```

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

```{code-cell} ipython3
try:
except OSError:
    raise RuntimeError from None # OSError was not preserved
```

```python
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
/tmp/ipykernel_70/669350098.py in <module>
      2     open('database.sqlite')
      3 except OSError:
----> 4     raise RuntimeError m
RuntimeError: 
```

+++

### User-defined Exceptions

```{code-cell} ipython3
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
        
class TransitionError(Error):
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

```{code-cell} ipython3
raise InputError("a", "message")
```

```python
---------------------------------------------------------------------------
InputError                                Traceback (most recent call last)
/tmp/ipykernel_31/1390501804.py in <module>
----> 1 raise InputError("a", "message")

InputError: ('a', 'message')
```

```{code-cell} ipython3
raise TransitionError("a", "b", "message")
```

```python
---------------------------------------------------------------------------
TransitionError                           Traceback (most recent call last)
/tmp/ipykernel_31/1582602960.py in <module>
----> 1 raise TransitionError("a", "b", "message")

TransitionError: ('a', 'b', 'message')
```

+++

### Defining Clean-up Actions

```{code-cell} ipython3
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```

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

```{code-cell} ipython3
def bool_return():
    try:
        return True
    finally:
        return False
    
bool_return()
```

```{code-cell} ipython3
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

```{code-cell} ipython3
divide(2,0)
```

```{code-cell} ipython3
divide(2,0)
```

```{code-cell} ipython3
divide('2', '1')
```

some objects have predefined clean up actions

```{code-cell} ipython3
for line in open('myfile.txt'):
    print(line, end=' ')
    
# this is brain-dead code, effectively leaving the file open
```

the following method has a `finally` statement built in such that the open file is always closed when the scope exited.

```{code-cell} ipython3
with open("myfile.txt") as f:
    for line in f:
        print(line, end=" ")
```

### References

1. [Errors and Exceptions -- Python Documentation](https://docs.python.org/3/tutorial/errors.html)

2. [Built-in Exceptions -- Python Documentation](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
