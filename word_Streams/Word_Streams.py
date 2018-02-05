
# coding: utf-8

# # Name Resolution

# In[95]:

import nltk
from nameparser.parser import HumanName


# In[198]:

import logging
import os
import glob2
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
import nltk
import re
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')',
                   '[', ']', '{', '}','%','&','+','$','@','~','-','_','://','--','[]','0','1','2','3','4','5','6','7','8','9']) # remove it if you need punctuation 
from nltk.tokenize import RegexpTokenizer
from datetime import datetime


# In[199]:

cd E:\task


# In[200]:

listdir = []
listdir = glob2.glob("*.txt")


# In[201]:

print(listdir)


# In[202]:

# iterate over the list getting each file
vocab = []
dic_tf = {}
dic_df = {}
for fle in listdir:
   # open the file and then call .read() to get the text 
   with open(fle) as f:
        text = f.read()
        print(text)
        s = text
        text = ' '.join(w for w in re.split(r"\W", s) if w)
        print(100)
        print(text)
        for tec in text:
            if tec.isdigit():
                    del tec
        for t in text:
            if t in stop_words:
                del t
            else: 
                if not t.isdigit():
                    t=t.lower()
            


# In[203]:

for t in text:
    if t.isdigit():
        del(t)


# In[204]:

text


# In[205]:

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)



# In[206]:

text[0]


# In[207]:

text


# In[208]:

names = get_human_names(text)


# In[209]:

print("LAST, FIRST")
for name in names: 
    last_first = HumanName(name).last + ', ' + HumanName(name).first
    print(last_first)


# # Another solution

# In[210]:

import nltk
def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))


# In[211]:

extract_entities(text)


# # solution #3

# In[249]:

for fle in listdir:
   # open the file and then call .read() to get the text 
   with open(fle) as f:
        text = f.read()
        s = text
        text = ' '.join(w for w in re.split(r"\W", s) if w)  
        text = wordpunct_tokenize(text)
        for tec in text:
            if tec in stop_words:
                del tec
        for tec in text:
            for t in tec:
                if t.isdigit():
                    del t
        
        for tec in text:
            for t in tec:
                if t not in stop_words: 
                    if not t.isdigit():
                        t=t.lower()
                


# In[250]:

text


# In[251]:

data = []
for t in text:
    data.append(extract_entities(t))


# In[ ]:



