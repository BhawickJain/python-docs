---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

## `Setup.py`

+++

`setup.py` is file that contains all the necessary information for a package installer to setup, compile and dsitribute the package. `setuptools` automate away the setup of a package during installation via package managers like `pip`. The `disutils` library helps distribute the module to package repos like PyPi.

```{code-cell} ipython3
!cat ../pyExamples/setup.py
```

```python
from setuptools import setup, find_packages


with open('README.md') as f:
     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='pyExamples',
    version='0.1.0',
    description='example code snippets to demonstrate software patterns in python',
    long_description=readme,
    author='Bhawick',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=('tests', 'docs')) # use find packages module 
                                                      # to install dependencies
                                                      # automatically, exclude
                                                      # test and doc folders.
)
```

+++

Much like `npm` `package.json` files in Javascript projects, you also setup comands which can be called in the following patten `python setup.py [command]`

This technically elleviates the need for `Makefile` but for the simplicity's sake and perhaps separating development details, it is used [2]. The following example demonstrates how you would include scripts in `setup.py`

+++

```python 
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='foomail@foo.com',
   url="http://www.foopackage.com/",
   packages=['foo'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)
```

+++

`pip install .`

+++

Avoid calling `setup.py` directly instead let the package manager like `pip` to handle the installation. The `setup.py` file indicates that the folder is a module/package to the package manager.

+++

`pip install -e .`

+++

During development use can also use the `-e` flag to install the package you are working on in development mode.

+++

Notice how when installed in development, python will now look at additional folders, including your local package folder when you reference (`from`/`import`) modules.

```{code-cell} ipython3
:tags: []

import sys
sys.path

# ['/data/nbs',
#  '/usr/local/lib/python39.zip',
#  '/usr/local/lib/python3.9',
#  '/usr/local/lib/python3.9/lib-dynload',
#  '',
#  '/usr/local/lib/python3.9/site-packages',
#  '/data/pyExamples',
#  '/usr/local/lib/python3.9/site-packages/IPython/extensions',
#  '/root/.ipython']
```

Common features in more advanced setup.py files is extraction of metadata is more user friendly places. For example, the version of a package may be placed in a single filea at the top level, which `setup.py` has to read and extract. Other problems could dependencies and tracing of versions, during package installation. In the `pytorch vision` `setup.py` the version file is written during installation to reflect the package but also indicate CUDA dependencies on the machine environment instelf.

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: []
---
from pyExamples import setuppy

?? setuppy.ex1_pytorch.clean
```

## References
1. [setup.py (for humans) -- Kenneth Reitz](https://github.com/kennethreitz/setup.py)
2. [FastAi Deep Learning LIbrary - Makefile -- Jeremy Howward, Seylvian Guggger (github)](https://github.com/fastai/fastai/blob/master/Makefile)
3. [Example of a real / advanced `setup.py` file -- (pytorch)](https://github.com/pytorch/vision/blob/master/setup.py)
4. [Python Packaging Using Guide -- (python.org)](https://packaging.python.org)
5. [Cookie Cutter PyPackage template -- Audrey Feldroy (github)](https://github.com/audreyfeldroy/cookiecutter-pypackage)
