
# coding: utf-8

# # Name Resolution

# In[1]:

import nltk
from nameparser.parser import HumanName


# In[2]:

import logging
import os
import glob2
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
import nltk
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
listdir = glob2.glob("*.xls")


# In[5]:

print(listdir)


# In[6]:

import pandas as pd


# In[7]:

text=pd.read_excel(listdir[0] )


# In[8]:

data = pd.DataFrame(text)


# In[9]:

data['WORD ']


# In[10]:

data['WORD ']


# # Another solution

# In[11]:

text = []
y = data['WORD ']
tokens = []
for i in range(len(y)):
    doc = y[i]
    if type(doc) != int:
        if doc.lower() not in stop_words:
            sentence = wordpunct_tokenize(doc)
            tokens.append(sentence)
            for j in range(len(sentence)):
                ken = sentence[j]
                if ken not in stop_words:
                    text.append(ken)


# In[12]:

tokens


# In[74]:

for toks in range(len(tokens)):
    dum = tokens[toks]
    for k in range(len(dum)):
        tec = dum[k]
        print(tec)
        if tec in stop_words:
                dum.remove(tec)


# # Which cleaning is better #1 or #2

# # clean_text#1

# In[75]:

def extract_entities(text):
    for chunk in nltk.ne_chunk(nltk.pos_tag(text)):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))


# # Cleaning as asked for

# In[76]:

tokens


# # Results not much expected but maybe better

# In[77]:

result = []
for toks in tokens:
    extract_entities(toks)


# # Concatenation of tuples to make a string as Ex: CA santoshkumardevri

# In[78]:

word_list = []
for toks in tokens:
    zecs = " ".join([str(i) for i in toks])
    word_list.append(zecs)


# In[79]:

word_list


# # Results are efficient and meaningful i think

# In[80]:

extract_entities(word_list)


# # clean_text#2

# In[81]:

text


# In[82]:

result = []
extract_entities(text)


# # Wigle Api Access

# In[83]:

from pygle import network


# In[84]:

network.geocode(addresscode="Delhi")


# In[85]:

"""
Sniff local WiFi networks in order to look them up on WiGLE.

"""
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


scan_cmd = {'windows': 'netsh wlan show networks mode=Bssid', 
            'linux': 'nmcli -t -f bssid dev wifi list',  # untested
            'osx': '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s',  # untested
            }


def local_bssids():
    """Get a list of available wireless access points.
    """
    res = subprocess.check_output(scan_cmd[system().lower()],
                                  universal_newlines=True)
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    bssids = pattern.findall(res)
    return set(bssids)


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
    if lats and longs:
        lat = sum(lats) / len(lats)
        lng = sum(longs) / len(longs)
        return lat, lng
    else:
        return "No geolocation possible"


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

