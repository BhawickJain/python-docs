```python
%config InlineBackend.figure_format = 'svg'
```

[[src](https://stackoverflow.com/questions/25412513/inline-images-have-low-quality)]


## Time Series Analysis with a NASA Dataset


Reference: [Time Series Analysis with Pandas - Manipulation and plotting of time series in python using Pandas methods -- Coding Club](https://ourcodingclub.github.io/tutorials/pandas-time-series/)

```python
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("pandas:", pd.__version__) # pandas: 1.3.2
print("numpy:", np.__version__) # numpy: 1.21.2
print("matplotlib", matplotlib.__version__) #matplotlib 3.4.3
```

### Retrieving the Dataset



```python
url = 'https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/omni2_all_years.dat'
path = './data/omni2_all_years.dat'
```

```python
# use bash function
#!wget url
```

```python
import requests
from pathlib import Path

def get_data_from_and_save(url, path):
    """
    Uses get requests library to download data and save to a particular location.
    
    Parameters
    ----------
    url (string): direct url to raw file
    path (string): target filepath (including name)
    """
    
    p  = Path(path)
    
    print("downloading file...")
    r = requests.get(url)
    print("file downloaded...")

    with open(p, "wb") as f:
        f.write(r.content)
        
# get_data_from_and_save(url, path) # get heliophysics dataset
```

```python
# direct download in to dataframe

df = pd.read_csv(url,
                 delim_whitespace=True,
                 usecols=[0, 1, 2, 39, 40, 50],
                 names=["year", "doy", "hour", "r", "dst", "f10.7"])
```

Alternative methods to download: [Download a csv from url and make it a dataframe python pandas -- stackoverflow](https://stackoverflow.com/questions/53158452/download-a-csv-from-url-and-make-it-a-dataframe-python-pandas)  
`[?]` Surely there is a better, more informative way to download larger files? Requirements: (1) Progress Bar, (2) Authentication, Exception Handling.


```python
df.head()
```

### Creating a datetime index

```python
def create_datestamp(year, doy, hour):
    """
    Takes year, day of year (doy) and hour and format to specific format
    
    The formats fits the year (four digits), day of year (three digits)
    and hours (2 digits) into a single string.
    YYYYjjjHH where j is the day of year.
    
    return
    ------
    formatted string datestamp
    """
    
    return year * 100000 + doy * 100 + hour
```

```python
df.index = pd.to_datetime(create_datestamp(df['year'], df['doy'], df['hour']), format="%Y%j%H")
df = df.drop(columns=['year', 'doy', 'hour'])
```

```python
df.head()
```

```python
df = df.replace({'r':999,
            'dst':99999,
            'f10.7':999.9}, np.nan)
df.head()
```

```python
print("Dataframe shape: ", df.shape)
dt = (df.index[-1] - df.index[0])
print("Number of hours between start and end dates: ", dt.total_seconds()/3600 + 1)
```

`[?]` Is there a better way to do that? or at least an alternative way?

```python
h, d, y = 24, 365, 55
print(f"{h} hours/day * {d} days/year * {y} years = {h*d*y} hours")
```

Given this dataset represents 55 years of hourly data, then why is there 517200 records (each representing an hour) when there can only be 481800 hours over that period. Is there a duplicate or an error somewhere?


### Plotting dataframe contents

```python
# define yticks
dst_yticks = [-600, -400, -200, 0]
r_and_f10_yticks = [0, 100, 200, 300]

# define data, labels, colors and yticks
data_labels = [('f10.7','F10.7', 'blue', r_and_f10_yticks), 
               ('dst', 'DST', 'orange', dst_yticks), 
               ('r', 'R', 'green', r_and_f10_yticks)]

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(12,6))
for i, ax in enumerate(axes):
    _ = ax.plot(data_labels[i][0], data=df, label=data_labels[i][1], c=data_labels[i][2])
    _ = ax.legend()
    _ = ax.set(yticks=data_labels[i][3])
    _ = ax.grid()
```

There is a lot of noise in the data.


`[?]` Any way to change the yticks?


### Resampling, rolling calculations, and differencing

```python
df[['f10.7', 'dst', 'r']].resample('1y').median().plot(figsize=(12,6))
```

```python
df[['f10.7', 'dst', 'r']].rolling(24*365).median().plot(figsize=(12,6))
```

```python
df[['f10.7', 'r', 'dst']].resample('3y').median().diff().plot(subplots=True, figsize=(12,6), grid=True)
```

### Identifying periodicity and correlation

```python

```
