# Question 1
import pandas as pd
dat = pd.read_csv("/depot/datamine/data/whin/190/combined.csv")
import plotly.express as px

def plot_stations(df, *ids):
    df = df.groupby("station_id").head(1).loc[df['station_id'].isin(ids), ('station_id', 'latitude', 'longitude')]
    fig = px.scatter_geo(df, lat="latitude", lon="longitude", scope="usa",
                     hover_name="station_id")
    fig.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['latitude'].iloc[0], lon=df['longitude'].iloc[0])))
    fig.show(renderer="jpg")
plot_stations(dat, 1,20,175)
Tuple = (1,20,175)
plot_stations(dat,*Tuple)
# The function aims takes the data set and a series of ids, scope the range to indiana, and only draw the stations which has id in the series that the function take. Layout is then modified and picture is shown in jpg format. Above both methods are tried, getting the same results.



# Question 2
dat.groupby(['station_id','latitude','longitude']).count().reset_index()
def plot_stations(df, weighted = False):
    if weighted:
        fig = px.scatter_geo(df.groupby(['station_id','latitude','longitude']).count().reset_index(), lat="latitude", lon="longitude", scope="usa",hover_name="station_id", size = 'id')
        fig.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['latitude'].iloc[0], lon=df['longitude'].iloc[0])))
    else:
        fig = px.scatter_geo(df.groupby('station_id').head(1), lat="latitude", lon="longitude", scope="usa",hover_name="station_id")
        fig.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['latitude'].iloc[0], lon=df['longitude'].iloc[0])))
    fig.show(renderer="jpg")
plot_stations(dat, weighted = False)
plot_stations(dat, weighted = True)
# Plots are created with weighted and not weighted.



# Question 3
def plot_stations(df, weighted = False, weight_by = None):
    if weighted and weight_by:
        fig = px.scatter_geo(df.groupby(['station_id','latitude','longitude']).median().reset_index(), lat="latitude", lon="longitude", scope="usa",hover_name="station_id", size = f'{weight_by}')
        fig.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['latitude'].iloc[0], lon=df['longitude'].iloc[0])))
    elif weighted and weight_by == None:
        fig = px.scatter_geo(df.groupby(['station_id','latitude','longitude']).count().reset_index(), lat="latitude", lon="longitude", scope="usa",hover_name="station_id", size = 'id')
        fig.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['latitude'].iloc[0], lon=df['longitude'].iloc[0])))
    else:
        fig = px.scatter_geo(df.groupby('station_id').head(1), lat="latitude", lon="longitude", scope="usa",hover_name="station_id")
        fig.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['latitude'].iloc[0], lon=df['longitude'].iloc[0])))
    fig.show(renderer="jpg")
plot_stations(dat, weighted=True, weight_by="temperature_high")
plot_stations(dat, weighted=True, weight_by="temperature_low")
plot_stations(dat, weighted=True, weight_by="wind_speed_high")
plot_stations(dat, weighted=False, weight_by="barometric_pressure")
plot_stations(dat, weighted=True, weight_by=None)
# All the plots are shown above.



# Question 4
my_df = pd.read_csv("depot/datamine/data/flights/subset/airports.csv")
my_df.head()
def mapping(df, *states):
    df = df.groupby("airport").head(1).loc[df['state'].isin(states), :]
    figure = px.scatter_geo(df.groupby('state').head(1), lat = 'lat', lon = 'long', hover_name = 'state', scope = 'usa')
    #figure.update_layout(geo = dict(projection_scale=7, center=dict(lat=df['lat'].iloc[0], lon=df['long'].iloc[0])))
    figure.show(renderer = "jpg")
states = ('IN','IL','AK','CA','MS','TX')
mapping(my_df, *states)
# As above, I use packing and unpacking states and mark the airport in the selected states.



# Question 5
WHIN = pd.read_csv('depot/datamine/data/whin/weather.csv')
WHIN.head()
WHIN = WHIN.drop_duplicates(subset = ["station_id"])
WHIN.head()
import numpy as np
def degrees_to_radians(value):
    return float(value * np.pi/180)
def get_distance(Ser1, Ser2):
    lat1 = degrees_to_radians(Ser1["latitude"])
    lat2 = degrees_to_radians(Ser2["latitude"])
    lon1 = degrees_to_radians(Ser1["longitude"])
    lon2 = degrees_to_radians(Ser2["longitude"])
    return 2*6367.4447*np.arcsin(np.sqrt(np.sin((lat2-lat1)/2)**2+np.cos(lat1)*np.cos(lat2)*np.sin((lon2-lon1)/2)**2))
location_list = []
for i in WHIN['station_id']:
    location = WHIN.loc[WHIN['station_id'] == i, :]
    location_list.append(location)
distance = []
for i in location_list:
    for j in location_list:
        distance.append(get_distance(i,j))
distance.sort(reverse=True)
distance[0:5]
# I calculated the top distances but have trouble with that line_geo function. I have no idea what is that "location" or "projection". Since it is optional, I think I practiced what I want already!





