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
# a    1.0
# b    2.0
# c    3.0
# d    4.0
# e    5.0
# dtype: float64
```

```python
s.dtype
# dtype('float64')
```

```python
s.index
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```

```python
s['c':'e']
# c    3.0
# d    4.0
# e    5.0
# dtype: float64
```

```python
s[2:4]
# c    3.0
# d    4.0
# dtype: float64
```

```python
s.iloc[2:4]
# c    3.0
# d    4.0
# dtype: float64
```

```python
t = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index=pd.date_range('1995-12-30', periods=5))
t
# 1995-12-30    1.0
# 1995-12-31    2.0
# 1996-01-01    3.0
# 1996-01-02    4.0
# 1996-01-03    5.0
# Freq: D, dtype: float64
```

```python
t['1996-01-01':'1996-01-03']
# 1996-01-01    3.0
# 1996-01-02    4.0
# 1996-01-03    5.0
# Freq: D, dtype: float64
```

```python
t[2:4]
# 1996-01-01    3.0
# 1996-01-02    4.0
# Freq: D, dtype: float64
```

```python
t.iloc[2:4]
# 1996-01-01    3.0
# 1996-01-02    4.0
# Freq: D, dtype: float64
```

`dataframe[start,end,stride]`  
Slicing by index number gives standard NumPy / Python Array Slicing Behaviour. However, when referring to an Index that is of a different data type such an object or datatime it will include the `end` value as well.


### Handling Datetime Index Series

```python
# 1995-12-06 is missing
dates = pd.date_range('1995-12-01', periods=5, freq='D')
dates = dates.append(pd.date_range('1995-12-07', periods=5, freq='D'))
values = [1,2,3,4,5,6,7,8,9,0]

miss_dates = pd.Series(values, index=dates)

miss_dates
# 1995-12-01    1
# 1995-12-02    2
# 1995-12-03    3
# 1995-12-04    4
# 1995-12-05    5
# 1995-12-07    6
# 1995-12-08    7
# 1995-12-09    8
# 1995-12-10    9
# 1995-12-11    0
# dtype: int64
```

For what `'D'` means check out the frequency offset aliases [[pd-docs-freq_str](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases)]

```python
miss_dates.asfreq('D')
# 1995-12-01    1.0
# 1995-12-02    2.0
# 1995-12-03    3.0
# 1995-12-04    4.0
# 1995-12-05    5.0
# 1995-12-06    NaN
# 1995-12-07    6.0
# 1995-12-08    7.0
# 1995-12-09    8.0
# 1995-12-10    9.0
# 1995-12-11    0.0
# Freq: D, dtype: float64
```

You can infer dates too

```python
miss_dates.asfreq(pd.infer_freq(miss_dates.index))
# 1995-12-01    1.0
# 1995-12-02    2.0
# 1995-12-03    3.0
# 1995-12-04    4.0
# 1995-12-05    5.0
# 1995-12-06    NaN
# 1995-12-07    6.0
# 1995-12-08    7.0
# 1995-12-09    8.0
# 1995-12-10    9.0
# 1995-12-11    0.0
# Freq: D, dtype: float64
```

### References



AstroTech Series Slicing [[astrotech-pd-series-slicing](https://pandas.astrotech.io/series/slice.html)]
