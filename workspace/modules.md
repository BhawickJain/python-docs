## Modules

Modules allow you to reuse multiple scripts by importing them where you need them in other scripts.

In the simplest form, you can import a `.py` file as a module as so:

```python
import fib
```

the name of the file becomes the name space under which all the functions and classes are accessible from the current symbol table.

```python
fib.fib(5)
```

```python
fib_seq = fib.fib2(5)
fib_seq
```

The module's name is generally inherited from the file name, but could be access and set within the `fib.py` and in this instance is called `fibo`.

```python
fib.__name__
```

There other ways to import


you can import `__all__` which is generally defined as all the attributes. But can also be set manually as found in the `fib.py` file. [[src](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)]

Notice how only `fib` is directly imported as set in `fib.py`. In addition all definitions that begin with `_` will not be imported.

```python
from fib import *
```

```python
fib(5)
```

Of course you can also import specific attributes directly, even something that hasn't been defined by `__all__`. So you can assume custom set `__all__` is the author's recommended import setting. Even still you wouldn't have to use `*` beyond experimentation.

```python
from fib import fib, fib2
```

```python
fib2(6)
```

You can also rename the attributes you're importing

```python
from fib import fib as fibonacci
```

You can run additional code that only runs when the module is run directly such as this:

```python
!python fib.py 50
```

### Module Search Path


### "Compiled" Python files


### Standard Modules


### The `dir()` Function


### Packages

A package is a series of modules with a `__init.py__` file which allow python to recognise the collection of modules to be part of a Package that is names after the enclosed folder.

```python
import sound.effects.echo as echo
```

notice how with each `dot` you it says that it is module, the `__init__.py` allows the folder to behave almost as though it is module as well. You could even further such as:

`import sound.effects.echo.some_function as some_function` as they all importable.

And much like in a module, you can define the `__all__` variable in the `__init__.py` to select particular modules when recommended imports are suggested.

```python
from sound import *
```

in this example, only `effects`, `filters`, `formats` are imported and `utils` is ignores because:

```python
!cat sound/__init__.py
#__all__ = ['effects', 'filters', 'formats']
```

### Intra-package References


Now that python intepreter understand the directly structure of the package, it can allow references to sibling sub-packages that sit under the main package. This how `test` modules can access the main module it is testing!

```python
from . import echo
from ..import formats
from ..filters import equalizer
```

`[ ]` See if you can get the `test_calc.py` module to be able to access the `calc.py` module
