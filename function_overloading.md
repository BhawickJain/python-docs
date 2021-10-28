---
jupyter:
  jupytext:
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

# Function Overloading (single and multiple dispatch)

Generally reserved for statically types languages, function overloading allows a function to share names with other funcitons which vary by their argument types. This had been extensively used in the [fast.ai deepl learning library](https://github.com/fastai/fastai/tree/master/fastai). Introducing function overloading is useful in python because is support one-obvious-way of doing something. The user of the fucntion does not have to choose a function according to the type being handled but instead simply choose according to a funcitonal need.


__Naive Approach__

```python
def add (a, b):
    if isinstance(a, str) or isinstance(b, str):
        return f'{a}{b}'
    elif isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        raise TypeError
```

Type-specific handling is handled by a careful check of what class the object is an instance of. This makes the code more complicated as it muddles two different types into in the same space. You also need additional if statements to handle the various combination of types and their handling. It also harder to document the logic as all there is only one docstring space to work with.

Ideally you want to use multiple functions of the same name each with independent handling per type. The Standard Library uses overloading all the time: `len()` or the arithmatic operators for strings and integers.

```python
'a' + 'b' #'ab'
'a' * 2   #'aa'
```

__Single Dispatch__

Single dispatch is natively supported by Python, unlike multiple dispatch

```python
from functools import singledispatch
from datetime import date, datetime, time

@singledispatch  # base implementation
def format(arg):
    return arg

@format.register
def _(arg: date):
    return f'{arg.day}-{arg.month}-{arg.year}'

@format.register
def _(arg: datetime):
    return f'{arg.day}-{arg.month}-{arg.year} {arg.hour}:{arg.minute}:{arg.second}'

@format.register(time)
def _(arg):
    return f'{arg.hour}:{arg.minute}:{arg.second}'
```

```python
print(format("today")) #today
```

```python
print(format(date(2021, 10, 28))) # 26-5-2021
```

```python
print(format(datetime(2021, 10, 28, 9, 10, 27))) # 28-10-2021 9:0:0
```

```python
print(format(time(19, 42, 45))) # 19:42:45
```

```python
from functools import singledispatchmethod
from datetime import date, time

class Formatter:
    
    @singledispatchmethod
    def format(self, arg):
        raise NoteImplementedError(f'Cannot format value of type {type(arg)}')
    
    @format.register
    def _(self, arg: date):
        return f'{arg.day}-{arg.month}-{arg.year}'

    @format.register(time)
    def _(self, arg):
        return f'{arg.hour}:{arg.minute}:{arg.second}'
```

```python
f = Formatter()
print(f.format(date(2021, 10, 28))) # 26-5-2021
print(f.format(time(19, 42, 45))) # 19:42:45
```

## Multiple Dispatch

Whilst `single` dispatch allows for a single type to be overloaded, `multipledispatch` allows allow multiple types to be defined for functions.

```python
!pip install multipledispatch
```

```python
from multipledispatch import dispatch

@dispatch(list, str)
def concatenate(a, b):
    a.append(b)
    return a

@dispatch(str, str)
def concatenate(a, b):
    return a + b

@dispatch(str, int)
def concatenate(a, b):
    return a + str(b)
```

```python
print(concatenate(["a", "b"], "c")) # ['a', 'b', 'c']
```

```python
print(concatenate("Hello", "World")) # HelloWorld
```

```python
print(concatenate("a", 1)) # a1
```

```python
from multipledispatch import dispatch

@dispatch((list, tuple), (str, int))
def concatenate(a, b):
    a.append(b)
    return a

@dispatch(str, str)
def concatenate(a, b):
    return a + b

@dispatch(str, int)
def concatenate(a, b):
    return a + str(b)
```

```python
# import Sequence which is the abstract base class for tuples, list and range
from collections.abc import Sequence

# isinstance does not work to see if list, typles are derived classes of Sequence:
isinstance(list, Sequence)
```

```python
from multipledispatch import dispatch

@dispatch(Sequence, (str, int))
def concatenate(a, b):
    a.append(b)
    return a

@dispatch(str, str)
def concatenate(a, b):
    return a + b

@dispatch(str, int)
def concatenate(a, b):
    return a + str(b)
```

Other considers are initialising classes with different types input types, i.e. overloading the `__init__`. But [this reference](https://stackoverflow.com/questions/141545/how-to-overload-init-method-based-on-argument-type/141777#141777) shows some way to tackle that.


__TODO__  
`[ ]` Create some personal examples of using operator overloading  
`[ ]` Check other professional code bases and see real examples of it, inc. fastai.  


## References

1. [The correct Way to Overload Functions -- Martin Heinz](https://towardsdatascience.com/the-correct-way-to-overload-functions-in-python-b11b50ca7336)
2. [Five-minute Multimethods Python -- Guide van van Rossum](https://www.artima.com/weblogs/viewpost.jsp?thread=101605)
