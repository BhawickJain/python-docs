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

## Arithmetic Operator Notation for improve UX

fastai uses a modified path library which allow the contentation of paths using the `__truediv__` symbol.

```python
class words:
    
    def __init__(self, word):
        self.word = word
        
    def __truediv__(self, other):
        return self.word + '/' + other
```

```python
one = words("hello")
one/'World'
```

The `cypython` `datetime` module offers similar facilities [src](https://github.com/python/cpython/blob/454cdb99abcda37413b15167cda564091fec2572/Lib/datetime.py#L650)
