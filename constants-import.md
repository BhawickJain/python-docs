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

### Defining and importing constants

Inpired by rubys/feedvalidator at [line 55](https://lgtm.com/projects/g/rubys/feedvalidator/snapshot/eb77aa864016e1071f37357746a3ad77de94432a/files/src/rdflib/syntax/parsers/RDFXMLHandler.py?sort=name&dir=ASC&mode=heatmap#L55)

You can import another file as a module and use the variables within as constants.

```python
from pyExamples.constants import C, PI, K, G
```

```python
G, C # Gravitational constant, Speed of Light
```

But is it _really_ a constant?

```python
G = 0
```

```python
G
```

In spite of being from another module, you can't make it immutable.


`[?]` How do you make an imported variable immutable?  
`[ ]` Maybe create a constants class?


Lets define Rydberg constant as `RINF`:

```python
RINF = 10e6 # painfully rough
```

Lets import the constant which holds a more accurate number.

```python
from pyExamples.constants import RINF
```

RINF already exists but is overwritten. In the past I have seen error being thrown because of this. It doesn't seem to happen all the time but its worth remembering the potential clash.

```python
RINF
```

Generally, you don't want to use `import`, especially `import *` as you are flooding your namespace with the `module`'s namespace. Thereby inadvertently overwriting and clashing stuff. So you want to do this:

```python
import pyExamples.constants as constants
constants.RINF
```

Another subtlety is that if you change `RINF` you don't change `constants.RINF`. So you can reimport the `constants` module and recover the number (without restarting the nb kernel). However if you change `constants.RINF` you change the module's variable value instead, no importing will work [[so-import-variables](https://stackoverflow.com/questions/17255737/importing-variables-from-another-file)].

```python
constants.RINF = 0
constants.RINF
```

```python
RINF
```

`[?]` Is there a way to force the rereading of the file?  
`>>>` Maybe but you don't want to allow the change in the first place. You need to modify how the `constant` module's attributes are modified.


### Class Attributes based - Constants


You can see that a constant can be overwritten even when coming from another module like `constant.RINF = 0`. This is because the `property()` function is still defined and leaves the object subject being changed. The `property` function manages the getting, setting, deleting of properties in the `__dict__` of the object. You can read more about it in [[py-docs-prop](https://docs.python.org/3/library/functions.html#property)].

```python
from pyExamples.constants import RINF
RINF
```

In `.src/const.py` there is a `const` class that holds all the attributes and manages then with its own get, set and delete attributes methods.

```python
import pyExamples.const as const
```

Here the `__setattr__` built-in function is involved thanks to the assignment operator used against the `const.RINF`. The functions overwrites the default `__setattr__` behaviour with its own by checking if attribute name exists in the `const` class symbol table (`const.__dict__`). If it does it throwns a custom `ConstError` otherwise goes ahead and assigns the name, value pair in the `const` class `__dict__`.

[[py-docs-abc](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)] Abstract base classes

```python
const.RINF = RINF
```

```python
const.RINF
```

If you reassign, the `__setattr__` is invoked again but this time, `RINF` already exists in the `const` class symbol table. Thereby throwing an error.

```python
# const.RINF = 80
# _ConstError
```

`line 23-24` in `src.const.py`overwrite the `syst.module.const` with the hidden `_const` class. This means any attributes added to `const` are instances of the `_const` instead of the `const.py` module. It means you can then enforce the `__setattr` functions against those attributes. Since the class and the constant error `_ConstError` class is hidden, only the constants are available to see.

Read more about `sys.modules` [[py-docs-sysmod](https://docs.python.org/3/library/sys.html#sys.modules)]

```python
type(const)
```

```python
const.__dict__
```

`[ ]` Disable `line 23-24` in `const.py`, restart the kernel and rerun the cells above. What is the difference and why? How come `const.RINF` is mutable?


### Class function based - Constants


[[py-docs-typefinal](https://docs.python.org/3/library/typing.html#typing.Final)] `typing.Final`  
[[so-creating-const](https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python?noredirect=1&lq=1) `Stackoverflow - Creating Constants`]


### Using `typing.final`

This is relatively new feature which was introduced in Python 3.8 [[pep-591](https://www.python.org/dev/peps/pep-0591/)].

```python
from typing import final
```

```python
JO: final = RINF
```

```python
JO
```

Tthe `typing.Final` does not inhibit mutability but instead get warned using static type checkers like [[`mypy`](http://mypy-lang.org/examples.html)].

```python
JO = 1
```

```python
JO
```

`[?]` Is defining constants a step away from idiomatic python coding style?


### Using @property decorator

[[ffc-propdeco](https://www.freecodecamp.org/news/python-property-decorator/)] The @property Decorator in Python: It Use Cases, Advantages, and Syntax  
[[zhou-decolev](https://medium.com/techtofreedom/7-levels-of-using-decorators-in-python-370473fcbe76)] 7 Levels of Using Decorators  
[[so-creating-const](https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python?noredirect=1&lq=1)] Stackoverflow - Creating Constants


```python
help(property)
```

`[?]` Can the `@property` decorator be used outside a class definition?

```python
import pyExamples.propconst as constp
```

```python
constp.PI
```

```python
# constp.PI = 60 # Attribute Error
```

The `constp` allows you to define all your constants as functions in one place. It uses the more pythonic `@` decorator which gives a very concise expression. Unlike `const` you can't define a new constant on the fly as you are not altering the `fget` and `fset` functions of how the class attributes are managed. This means you can create a new attribute against the class which isn't a constant.

```python
constp.ETA = 70
```

One could disallow that by defining a `__setattr__` as raising an error. Uncomment the `__setattr__` definition in the `propconst.py` file, reimport and rerun the statement above. But _feels_ this is less elegant.
