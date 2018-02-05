
# coding: utf-8

# In[2]:

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

data = pd.read_csv("../input/NYC_Wi-Fi_Hotspot_Locations.csv")
data.head()


# Looking at the Neighborhood Tabular Areas (a type of neighborhood area designation used by the City of New York) assigned to the various WiFi nodes, we see that far and away the most "popular" areas for putting up a hotspot are in Manhattan.

# In[3]:

data['NTAName'].value_counts()


# A tabulation by borough shows this even more clearly:

# In[4]:

data['Borough'].value_counts().plot.bar()


# We can get a better feel for what the distribution is with a quick map:

# In[5]:

import folium
display = folium.Map(location=[40.75, -74])

for (_, (lat, long)) in data[['Latitude', 'Longitude']].iterrows():
    folium.CircleMarker([lat, long],
                    radius=5,
                    color='#3186cc',
                    fill_color='#3186cc',
                   ).add_to(display)

display


# The WiFi hotspots are (logically) concentrated alongside certain arterial roadways. What stands out is how strong that effect is. 3rd Avenue and 8th Avenue in Manhattan both "stand out" in terms of their WiFi offerings, as do certain other roadways, like Queens Boulevard.

# What happens when we try to cluster?

# In[6]:

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=8, random_state=0).fit(data[['Latitude', 'Longitude']].values)
labels = kmeans.labels_

colors = ['#d53e4f','#f46d43','#fdae61','#fee08b','#e6f598','#abdda4','#66c2a5','#3288bd']
display = folium.Map(location=[40.75, -74])

for (lat, long, label) in zip(data['Latitude'], data['Longitude'], labels):
    folium.CircleMarker([lat, long],
                    radius=5,
                    color=colors[label],
                    fill_color=colors[label],
                   ).add_to(display)
    
display


# Interestingly enough, KMeans clustering (a decent default) doesn't stop on the borough boundaries quite like I thought it would, instead pushing into "uptownsy" (and popular!) parts of Brooklyn and Queens close to Manhattan as well. This is evidence that unlike certain other projects, public WiFi "pushes out" past Manhattan and into the outer boroughs as well, at least a little.
# 
# The vast majority of nodes in New York City are provided by the same entity, LinkNYC:

# In[7]:

data['Provider'].value_counts()


# It turns out that LinkNYC is also responsible for much of the street-structuring of the data!

# In[8]:

from sklearn.cluster import KMeans
selection = data[data['Provider'] == 'LinkNYC - Citybridge']
kmeans = KMeans(n_clusters=5, random_state=0).fit(selection[['Latitude', 'Longitude']].values)
labels = kmeans.labels_

colors = ['#d7191c','#fdae61','#ffffbf','#abdda4','#2b83ba']
display = folium.Map(location=[40.75, -74])


for (lat, long, label) in zip(selection['Latitude'], selection['Longitude'], labels):
    folium.CircleMarker([lat, long],
                    radius=5,
                    color=colors[label],
                    fill_color=colors[label],
                   ).add_to(display)
    
display

