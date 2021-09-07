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


### Plotting dataframe contents
