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
```

```python
!mypy headlines.py
```

<!-- #region -->
```bash
Success: no issues found in 1 source file
```
<!-- #endregion -->

Gradual typing is the practice of bringing in types as the code base matures, part of it need unit tests and are critical components.


Annotations are available with the use of type hinting

```python
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
<!-- #endregion -->

```python
!mypy headlines-python2.py
```

### References

1. [the state of type hints in python -- Bernát Gábor](https://bernat.tech/posts/the-state-of-type-hints-in-python)
2. 
