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

## Typing


### Type Hinting

Python and programmer reading it will be `type` aware allowing python to inform potential misuse of the code. Generally python is all about duck typing so if variation in the type doesn't matter, it won't care. In places it does, type hinting is useful, but won't be enforced.

```python
def greet(name: str) -> str:
    return "Hello, " + name
```

```python
def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")
```

```python
print(headline("python type checking"))
```

```python
print(headline("python type checking", False))
```

typed version

```python
def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")
```

### Mypy

```python
!pip install mypy
!mypy --version
```

```python
!mypy ../pyExamples/headlines.py
```

<!-- #region -->
```bash
Success: no issues found in 1 source file
```
<!-- #endregion -->

Gradual typing is the practice of bringing in types as the code base matures, part of it need unit tests and are critical components.


Annotations are available with the use of type hinting

```python
---------
```

<!-- #region -->
**Target Behaviour**
```python
>>> from pyExamples import typing
This is the typing tutorial

>>> typing.ex1_type_hinting
prints example results

>>> typing.ex1_typing_hinting.headline("hello")
```
<!-- #endregion -->

```python
----
```

This is an example of just importing a feature module from the `pyExample` package. This will only run its `__init__` file so

```python
from pyExamples import typing
```

```python
??typing
```

```python tags=[]
dir()
```

```python
??typing.type_annotation
```

The example below we are importing only the `__all__` attributes, which defined in teh `__init__.py` file but otherwise none of the import code in the `__init__.py` was imported. In addition, `attributes` of `pyExamples.typing` were directly imported so the `typing` namespace does not need to be referred to. I don't prefer that but it is useful to know.

```python
from pyExamples.typing import *
```

```python tags=[]
dir()
```

```python
??type_annotation
```

```python
??type_hinting
```

```python tags=[]
dir()
```

```python
import pyExamples.typing.ex1_type_hinting as ex1_type_hinting

ex1_type_hinting.headline("hello")
```

```python
import pyExamples.typing as typing

# typing.ex1_type_hinting.headline("hello")
```

```python
from pyExamples import typing

headline = typing.type_hinting.headline
headline.__annotations__
# {'text': str, 'align': bool, 'return': str}
```

### Type Annotations in legacy code

<!-- #region -->
Type Comments is a practice of hinting types in `python2` code which is generally unable to support type hinting. For example:

```python
def healine1(text, width==80, fill_char="-"):
    #type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)

```{code-cell} ipython3
!mypy headlines-python2.py
```

`[ ]` `mypy` could be run as part of `make test`
<!-- #endregion -->

### References

1. [the state of type hints in python -- Bernát Gábor](https://bernat.tech/posts/the-state-of-type-hints-in-python)
