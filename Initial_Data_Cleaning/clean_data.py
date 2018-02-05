
# coding: utf-8

# # Name Resolution

# In[4]:

import nltk
from nameparser.parser import HumanName


# In[174]:

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


# In[33]:

cd E:\task


# In[53]:

listdir = []
listdir = glob2.glob("*.xls")


# In[54]:

print(listdir)


# In[55]:

import pandas as pd


# In[56]:

text=pd.read_excel(listdir[0] )


# In[57]:

data = pd.DataFrame(text)


# In[58]:

data['WORD ']


# In[276]:

data['WORD ']


# # Another solution

# In[219]:

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


# In[235]:

tokens


# In[274]:

for toks in range(len(tokens)):
    dum = tokens[toks]
    for k in range(len(dum)):
        tec = dum[k]
        if tec in stop_words:
                dum.remove(tec)


# # Which cleaning is better #1 or #2

# # clean_text#1

# In[275]:

tokens


# # clean_text#2

# In[216]:

text


# In[214]:

def extract_entities(text):
    for chunk in nltk.ne_chunk(nltk.pos_tag(text)):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))


# In[215]:

result = []
extract_entities(text)

