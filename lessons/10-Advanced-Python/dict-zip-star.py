
# coding: utf-8

# In[2]:


import os
# !pip install seaborn
import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# !pip install mpld3
import mpld3
import json

pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 10)
get_ipython().magic('matplotlib inline')
mpld3.enable_notebook()


# In[23]:


# Let's talk about dict and zip
dict([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)])


# In[1]:


# zip can create that pairing for us by zippering up two sides (lists) together
zipped = zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4])
print(zipped)


# In[ ]:





# In[24]:


# dict will accept any sequences of pairings (2-tuples)
# but what if we have two sequences of values that we want to "pair up"
# zip brings the two sides of a pair (the sides of a zipper) together in an alligned pairing
list(zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))


# In[25]:


# and a dict is can take a list of pairs, like before... so
dict(zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))


# In[26]:


# and `range(5)` is a sequence (iterable)
dict(zip(['a', 'b', 'c', 'd', 'e'], range(5)))


# In[27]:


# if we get the length wrong, the zipper will get "stuck" on the shortest sequence
dict(zip(['a', 'b', 'c', 'd', 'e'], range(4)))


# In[28]:


# or because any sequence will do, and a str is a sequence of characters:
dict(zip('abcde', range(5)))


# In[29]:


# What will happen if you try to coerce a list of 3-tuples into a dict?
dict([('a', 1, 2), ('b', 3, 4)])


# In[30]:


x = list(range(3))
y = list(range(4))
print(x)
print(y)
list(zip(x, y, range(5)))


# In[31]:


x = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
list(zip(*x))


# In[32]:


list(zip(x[0], x[1], x[2]))

