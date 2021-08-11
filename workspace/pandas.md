## Pandas

```python
import pandas as pd
pd.__version__ #1.3.1
```

### Slicing indexes of different datatypes

```python
s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index=['a', 'b', 'c', 'd', 'e'])

s
```

```
a    1.0
b    2.0
c    3.0
d    4.0
e    5.0
dtype: float64
```

```python
s.dtype
```

```python
s.index
```

```python
s['c':'e']
```

```python
s[2:4]
```

```python
s.iloc[2:4]
```

```python
t = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index=pd.date_range('1995-12-30', periods=5))
t
```

```python
t['1996-01-01':'1996-01-03']
```

```python
t[2:4]
```

```python
t.iloc[2:4]
```

`dataframe[start,end,stride]`  
Slicing by index number gives standard NumPy / Python Array Slicing Behaviour. However, when referring to an Index that is of a different data type such an object or datatime it will include the `end` value as well.

```python

```
