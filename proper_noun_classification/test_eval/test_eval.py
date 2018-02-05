
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np
import os

import data_utils


# In[2]:


test_filename = "pnp-test.txt"

file_path = os.path.join(os.path.abspath(os.path.curdir), test_filename)
f = open(file_path, 'r', encoding = "ISO-8859-1")
data = list(f.readlines())
f.close()
data = [s.strip().split() for s in data]


# In[3]:


data[0][0]


# In[4]:


proper_nouns_strings = [" ".join(d[1:]) for d in data]

print(proper_nouns_strings)


# In[5]:


f = open("output.txt", 'w', encoding = "ISO-8859-1")
for noun in proper_nouns_strings:
    f.write("Example: "+noun+" guess="+" drug "+" gold= confidence="+str(10)+"\n")
f.close()


# In[6]:


len(proper_nouns_strings)


# In[7]:


import os

