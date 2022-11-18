# Question 1
import pandas as pd
stations = pd.read_csv("/depot/datamine/data/whin/190/stations.csv")
obs = pd.read_csv("/depot/datamine/data/whin/190/observations.csv")
stations.head()
obs.head()
dat = obs.merge(stations, how = "left", left_on = "station_id", right_on = "id")
dat = dat.drop(columns = "id_y")
dat = dat.rename(columns = {"id_x": "id", "name": "station_name"})
dat.head()
# All the operations are done above.


# Question 2
from cyksuid import ksuid
dat["id"].sample(10).tolist()
def get_datetime(Str):
    return ksuid.parse(Str.replace("obs_" , "")).datetime
Value = sorted(dat["id"].sample(10).tolist())
for val in Value:
    print(get_datetime(val))
# As we can see, the time is sorted and from the earliest to the latest.



# Question 3
import numpy as np
def degrees_to_radians(value):
    return float(value * np.arctan2(0,-1)/180)
degrees_to_radians(88.0)
# Result is listed above.



# Question 4
def degrees_to_radians(value):
    return float(value * np.arctan2(0,-1)/180)
def get_distance(Ser1, Ser2):
    lat1 = degrees_to_radians(dat.loc[dat["id"] == Ser1, "latitude"])
    lat2 = degrees_to_radians(dat.loc[dat["id"] == Ser2, "latitude"])
    lon1 = degrees_to_radians(dat.loc[dat["id"] == Ser1, "longitude"])
    lon2 = degrees_to_radians(dat.loc[dat["id"] == Ser2, "longitude"])
    return 2*6367.4447*np.arcsin(np.sqrt(np.sin((lat2-lat1)/2)**2+np.cos(lat1)*np.cos(lat2)*np.sin((lon2-lon1)/2)**2))
get_distance("obs_1amnn4xst3O9VOawmUHFiqBVnCK", "obs_1fwlznMZXXS8WBkmyTHRgWnHYYf")
location1 = dat.loc[dat['id']=="obs_1amnn4xst3O9VOawmUHFiqBVnCK", :]
location2 = dat.loc[dat['id']=="obs_1fwlznMZXXS8WBkmyTHRgWnHYYf", :]
def get_distance(Ser1, Ser2):
    lat1 = degrees_to_radians(Ser1["latitude"])
    lat2 = degrees_to_radians(Ser2["latitude"])
    lon1 = degrees_to_radians(Ser1["longitude"])
    lon2 = degrees_to_radians(Ser2["longitude"])
    return 2*6367.4447*np.arcsin(np.sqrt(np.sin((lat2-lat1)/2)**2+np.cos(lat1)*np.cos(lat2)*np.sin((lon2-lon1)/2)**2))
get_distance(location1, location2)
# Here are 2 ways to do the problem. Same idea but different processes.



# Question 5
import plotly.express as px
def plot_stations(dat):
    dat['position'] = dat['latitude'].astype(str) + dat['longitude'].astype(str)
    figure = px.scatter_geo(dat.groupby(['position']).head(1), lat = 'latitude', lon = 'longitude', hover_name = "station_id", scope = 'usa')
    figure.update_layout(title = 'World Map', title_x = 0.5)
    return figure.show()
plot_stations(dat)
# Function is created and plot was zoomed in.



