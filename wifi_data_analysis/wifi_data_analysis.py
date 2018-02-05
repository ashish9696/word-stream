
# coding: utf-8

# In[1]:

import nltk
from nameparser.parser import HumanName


# In[6]:

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


# In[3]:

cd E:\task


# In[4]:

listdir = []
listdir = glob2.glob("*.txt")


# In[5]:

listdir


# In[10]:

data = pd.read_csv(listdir[0], sep="`", header=None)


# In[12]:

data.columns = ["time", "range", "bssid", "type", "name", "etc1", "etc2"]


# In[13]:

data


# In[24]:

data['time'] = pd.to_datetime(data['time'])


# In[27]:

data['time']


# In[26]:

data['new_date'] = [d.date() for d in data['time']]
data['new_time'] = [d.time() for d in data['time']]


# In[28]:

data


# In[35]:

df = data
df['Year'] = df['time'].dt.year
df['Month'] = df['time'].dt.month
df['Day'] = df['time'].dt.day
df['hour'] = df['time'].dt.hour
df['minute'] = df['time'].dt.minute


# In[36]:

df


# In[39]:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from platform import system
import re
import subprocess
import time

import requests

from pygle import network


# In[38]:

network.geocode(addresscode="Delhi")


# In[51]:

res = network.search(netid='84:3a:4b:04:d6:66')


# In[54]:

res


# In[47]:

scan_cmd = {'windows': 'netsh wlan show networks mode=Bssid', 
            'linux': 'nmcli -t -f bssid dev wifi list',  # untested
            'osx': '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s',  # untested
            }


def local_bssids():
    """Get a list of available wireless access points.
    """
    res = df['bssid']
    bssids=[]
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    for r in df['bssid']:
        bssids.append(pattern.findall(r))
    return bssids


def geolocate():
    """Locate a device using locally available wireless access points.
    """
    lats = []
    longs = []
    for bssid in local_bssids():
        print("BSSID:", bssid)
        lat, lng = geolocate_wigle(bssid)  # can be replaced with other geocoding sources
        if lat and lng:
            lats.append(lat)
            longs.append(lng)
        time.sleep(0.1)

def geolocate_wigle(bssid):
    """Search WiGLE for a BSSID and return lat/lng.
    """
    res = network.search(netid=bssid)
    if res['success'] and res['resultCount']:
        lat = res['results'][0]['trilat']
        lng = res['results'][0]['trilong']
    else:
        print(res)
        lat, lng = None, None
    return lat, lng


if __name__ == "__main__":
    print("WiGLE")
    print(geolocate())

