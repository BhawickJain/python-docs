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

```python
%config InlineBackend.figure_format = 'retina'
```

```python
class PRG:

    def __init__(self, seed):
        self.seed = seed

    def _middle_square_implementation(self, seed, prn_length):
        assert len(str(seed))!=prn_length, ValueError
        square = seed**2
        str_square = str(square).zfill(prn_length*2)
        start = int((len(str_square)-prn_length)/2)
        middle = int(str_square[start:prn_length+1])
        return middle, middle
    
    @classmethod
    def middle_square(cls,seed):
        state = seed
        while True:
            state, prn = cls._middle_square_implementation(state, prn_length=len(str(state)))
            yield prn

    @classmethod
    def wichmannhill(cls):
        state, prn = _wichmannhill_implementation(seed)
        yield prn

    def generate(self, generator=middle_square):
        return generator(self.seed)
```

```python
prn = PRG(44567)
prn_generator = prn.generate()
next(prn_generator)
```

```python
a = PRG.middle_square(45)
next(a)
```

```python jupyter={"outputs_hidden": true} tags=[]
import pandas as pd
import matplotlib as plt

def generate_show_prns(seed, iterations=1000):
    prn = PRG(seed)
    prn_generator = prn.generate()
    middle_square_gen_numbers = pd.DataFrame([next(a) for i in range(iterations)])
    middle_square_gen_numbers.reset_index().plot(kind='scatter', x='index', y=0)

generate_show_prns(445678)
generate_show_prns(5)
generate_show_prns(78)
generate_show_prns(778)
```

```python
prn = PRG(50)
prn_generator = prn.generate()
middle_square_gen_numbers = pd.DataFrame([next(a) for i in range(10)])
middle_square_gen_numbers
```

```python
def natural_numbers():
   num = 1
   while num <= 50:
       yield num
       num += 1
        
a = natural_numbers()
```

```python
print(next(a))
```

```python
next(natural_numbers())
```

```python
def add(a, b): return a + b
addition = add
addition(1,2)
```

```python tags=[]
class PRG:
    
    @staticmethod
    def increment(state):
        """
        Dummy Algorithm
        """
        return state + 1
    
    @staticmethod
    def middle_square(state):
        """
        Von Neumann's Middle Square Pseudo Random Number Generator
        """
        square = str(state**2)
        square_zfilled = square.zfill(len(str(state)*2))
        return int(square_zfilled[int(len(str(state))/2):len(str(state))+1])
    
    def generator(self):
        while True:
            self._state =  self.algorithm(self._state)
            yield self._state

    # __func__ https://stackoverflow.com/questions/12718187/calling-class-staticmethod-within-the-class-body
    def __init__(self, seed, algorithm=increment.__func__):
        self.seed = seed
        self._state = seed
        self.algorithm = algorithm
        

        
```

```python
seed =7058693086
random_number_object = PRG(seed, PRG.middle_square)
random_number_generator = random_number_object.generator()
```

```python
next(random_number_generator)
```

```python
PRG.increment(50)
```

```python
705**2
```

```python
str(705**2).zfill(6)
```

```python
int(len(str(state))/2-1):len(str(state))
```

```python

```
