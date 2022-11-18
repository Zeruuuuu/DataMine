# Question 1
import pandas as pd
import numpy as np
from pathlib import Path
csv_files = Path('/depot/datamine/data/disney').glob('*.csv')
data = pd.DataFrame()
for csv in csv_files:
    if csv.name == 'metadata.csv' or csv.name == 'entities.csv':
        continue
    df = pd.read_csv(csv)
    df['ride_name'] = csv.name.split('.')[0]
    data = pd.concat([data,df])
data.head()
data = data.drop(columns = ['date'])
data.head()
data['status'] = 'open'
data.loc[data['SPOSTMIN'] == -999, "status"] = "closed"
data.loc[data['SPOSTMIN'] == -999, "SPOSTMIN"] = np.nan
data.head()
data['datetime'] = pd.to_datetime(data['datetime'])
data['ride_name'] = data['ride_name'].astype("category")
data['status'] = data['status'].astype("category")
print(data.dtypes)
data.reset_index(drop = True, inplace = True)
data.tail()
# As code above, data is prepared.


# Question 2
data.groupby("ride_name").mean().sort_values('SACTMIN', ascending = False)
# As above, mean is calculated and sorted.


# Question 3
dat = data.groupby("ride_name")['SPOSTMIN'].median()
dat.plot.bar()
import plotly.express as px
fig = px.bar(data.groupby("ride_name")['SPOSTMIN'].median())
fig.show(renderer = 'jpg')
# As above, two bar plot are created.


# Question 4
def min_to_hr(minute):
    return minute/60.0
data.groupby('ride_name').median().apply(min_to_hr).query("SPOSTMIN >= 1")
# Apply and query commands are used.



# Question 5
data.assign(mean_wait_time_act = lambda x: x.groupby('ride_name')['SACTMIN'].transform('mean') )
data.assign(mean_wait_time_post = lambda x: x.groupby('ride_name')['SPOSTMIN'].transform('mean'))
data.assign(median_wait_time_act = lambda x: x.groupby('ride_name')['SACTMIN'].transform('median'))
data.assign(median_wait_time_post = lambda x: x.groupby('ride_name')['SPOSTMIN'].transform('median'))
# Four new columns are listed above.

