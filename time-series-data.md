## Time Series Data

```python
import pandas as pd
from datetime import datetime
import numpy as np
```

Create a Date Range

```python
a_date_range = pd.date_range(start='1/1/2018', end='1/08/2018', freq='H')
a_date_range

# DatetimeIndex(['2018-01-01 00:00:00', '2018-01-01 01:00:00',
#                '2018-01-01 02:00:00', '2018-01-01 03:00:00',
#                '2018-01-01 04:00:00', '2018-01-01 05:00:00',
#                '2018-01-01 06:00:00', '2018-01-01 07:00:00',
#                '2018-01-01 08:00:00', '2018-01-01 09:00:00',
#                ...
#                '2018-01-07 15:00:00', '2018-01-07 16:00:00',
#                '2018-01-07 17:00:00', '2018-01-07 18:00:00',
#                '2018-01-07 19:00:00', '2018-01-07 20:00:00',
#                '2018-01-07 21:00:00', '2018-01-07 22:00:00',
#                '2018-01-07 23:00:00', '2018-01-08 00:00:00'],
#               dtype='datetime64[ns]', length=169, freq='H')
```

```python
type(a_date_range[0])
# pandas._libs.tslibs.timestamps.Timestamp
```

```python
df = pd.DataFrame(a_date_range, columns=['date'])
df['data'] = np.random.randint(0,100, size=(len(a_date_range)))

print(df.head(15))


#                   date  data
# 0  2018-01-01 00:00:00    99
# 1  2018-01-01 01:00:00    15
# 2  2018-01-01 02:00:00    79
# 3  2018-01-01 03:00:00    37
# 4  2018-01-01 04:00:00    27
# 5  2018-01-01 05:00:00    51
# 6  2018-01-01 06:00:00    20
# 7  2018-01-01 07:00:00    87
# 8  2018-01-01 08:00:00    86
# 9  2018-01-01 09:00:00    31
# 10 2018-01-01 10:00:00    29
# 11 2018-01-01 11:00:00    74
# 12 2018-01-01 12:00:00     8
# 13 2018-01-01 13:00:00    95
# 14 2018-01-01 14:00:00    42
```

```python
df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True) # remove all columns (axis=1) under column label 'date'
print(df.head())

#                     data
# datetime                 
# 2018-01-01 00:00:00    45
# 2018-01-01 01:00:00    18
# 2018-01-01 02:00:00    34
# 2018-01-01 03:00:00     4
# 2018-01-01 04:00:00    39
```

```python
df.index.dtype
```

Convert string to datetime

```python
string_date_range = [str(s) for s in a_date_range]

timestamp_date_range = pd.to_datetime(string_date_range, infer_datetime_format=True)
print(timestamp_date_range)
```

Generally you want to be more explicit on your datetime conversion to prevent inference from being in consistent.

```python
string_date_range_two = ['June-01-2018', 'June-02-2018', 'June-02-2018', 'June-03-2018']
timestamp_date_range_two = [datetime.strptime(x, '%B-%d-%Y') for x in string_date_range_two]

# [datetime.datetime(2018, 6, 1, 0, 0),
#  datetime.datetime(2018, 6, 2, 0, 0),
#  datetime.datetime(2018, 6, 2, 0, 0),
#  datetime.datetime(2018, 6, 3, 0, 0)]
```

```python
print(df.resample('D').mean())

#                  data
# datetime             
# 2018-01-01  49.000000
# 2018-01-02  42.333333
# 2018-01-03  54.875000
# 2018-01-04  50.083333
# 2018-01-05  48.666667
# 2018-01-06  46.583333
# 2018-01-07  48.208333
# 2018-01-08  27.000000
```

Is this is the oppposite of `pd.asfreq` function?

```python
df['rolling_sum'] = df.rolling(3).sum()
print(df.head(10))

#                      data  rolling_sum
# datetime                              
# 2018-01-01 00:00:00    45          NaN
# 2018-01-01 01:00:00    18          NaN
# 2018-01-01 02:00:00    34         97.0
# 2018-01-01 03:00:00     4         56.0
# 2018-01-01 04:00:00    39         77.0
# 2018-01-01 05:00:00    60        103.0
# 2018-01-01 06:00:00    26        125.0
# 2018-01-01 07:00:00    80        166.0
# 2018-01-01 08:00:00    47        153.0
# 2018-01-01 09:00:00    86        213.0
```

```python
df['rolling_sum'].fillna(method='backfill')

# datetime
# 2018-01-01 00:00:00     97.0
# 2018-01-01 01:00:00     97.0
# 2018-01-01 02:00:00     97.0
# 2018-01-01 03:00:00     56.0
# 2018-01-01 04:00:00     77.0
#                        ...  
# 2018-01-07 20:00:00    122.0
# 2018-01-07 21:00:00    175.0
# 2018-01-07 22:00:00    109.0
# 2018-01-07 23:00:00    165.0
# 2018-01-08 00:00:00    131.0
# Name: rolling_sum, Length: 169, dtype: float64
```

```python
epoch_t = 1529272655
real_t = pd.to_datetime(epoch_t, unit='s')
real_t

# Timestamp('2018-06-17 21:57:35')
```

```python
real_t.tz_localize('UTC')  # set timezone attribute to UTC
# Timestamp('2018-06-17 21:57:35+0000', tz='UTC')

real_t.tz_localize('UTC').tz_convert('US/Pacific') # convert timezone from current attribute to another
# Timestamp('2018-06-17 14:57:35-0700', tz='US/Pacific')
```

Points to keep in mind during the preprocessing:
1. Check for datetime format discrepencies: sudden changes from British to American datetime format are the worst kinds. So are things like changes to the timezone or daylight savings.
2. Keep track of timezones: particularly when the time is reported in relation to local time which is typical of international modes of travel.
3. Missing data, be able to justify by forward / backward fill is appropriate or any other decision.
4. Keep track of each transformation as functions that can be documented, called upon and applied.
5. Justify any resampling carefully.


### Reference

1. [Basic Time Series Manipulation with Pandas](https://towardsdatascience.com/basic-time-series-manipulation-with-pandas-4432afee64ea)
2. [Time Series Analysis with Pandas - Manipulation and Plotting of Time Series in Python using Pandas Methods](https://ourcodingclub.github.io/tutorials/pandas-time-series/)
