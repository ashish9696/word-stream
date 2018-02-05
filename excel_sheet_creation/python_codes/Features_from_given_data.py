
# coding: utf-8

# # Import Packages

# In[63]:

import nltk
from nameparser.parser import HumanName


# In[64]:

import logging
import os
import glob2
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
import nltk
import pandas as pd
import re
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')',
                   '[', ']', '{', '}','%','&','+','$','@','~','-','_','://','--','[]','`']) # remove it if you need punctuation 
from nltk.tokenize import RegexpTokenizer
from datetime import datetime


# # Library setup

# In[65]:

cd E:\task


# In[66]:

listdir = []
listdir = glob2.glob("*.txt")


# In[67]:

listdir


# In[68]:

data = pd.read_csv(listdir[0], sep="`", header=None)


# In[69]:

data.columns = ["time", "range", "bssid", "type", "name", "etc1", "etc2"]


# In[70]:

data


# In[71]:

data.to_csv("input_data.csv", index=False)


# In[73]:

inp = pd.read_csv( "input_data_with_lat_lon.csv" )


# In[74]:

inp


# In[75]:

inp['lat']


# In[76]:

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)


# # Now try to get some features via lat lon

# In[80]:

import geocoder
for i in range(len(inp)):
    l = inp['lat'][i]
    k = inp['lon'][i]
    location = geocoder.google([l , k], method='reverse')
    inp['city'][i] = location.city
    inp['state'][i] = location.state
    inp['state_long'][i] = location.state_long
    inp['country'][i] = location.country
    inp['country_long'][i] = location.country_long


# In[79]:

inp['city'] = location.city
inp['state'] = location.state
inp['state_long'] = location.state_long
inp['country'] = location.country
inp['country_long'] = location.country_long


# In[81]:

data = inp
data


# In[82]:

data['time'] = pd.to_datetime(data['time'])


# In[83]:

data['new_date'] = [d.date() for d in data['time']]
data['new_time'] = [d.time() for d in data['time']]


# In[84]:

data


# In[86]:

import sys
import operator
import pandas as pd
import numpy as np
from sklearn import preprocessing, model_selection, metrics, ensemble
import xgboost as xgb


# # Features

# In[87]:

df = data
df['Year'] = df['time'].dt.year
df['Month'] = df['time'].dt.month
df['Day'] = df['time'].dt.day
df['hour'] = df['time'].dt.hour
df['minute'] = df['time'].dt.minute


# In[88]:

df


# In[90]:

df.to_csv("output_featured.csv")

