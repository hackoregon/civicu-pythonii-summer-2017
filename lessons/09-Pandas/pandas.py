
# coding: utf-8

# In[33]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import seaborn
import json

pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 10)
get_ipython().magic(u'matplotlib inline')
mpld3.enable_notebook()


# In[7]:


# df = pd.read_csv('../shared-resources/crimedata.csv')
df = pd.DataFrame.from_csv('../shared-resources/crimedata.csv', index_col=0)
df.tail()


# ### Lets set our index to the `report_date` column
# (the 3rd column, or column number 2, in our CSV)

# In[9]:


df = pd.DataFrame.from_csv('../shared-resources/crimedata.csv', index_col=2)
df.tail()



# In[10]:


# Now we can retrieve all the crimes on a particular date just by using the `.loc` getitem method (square brackets)
df.loc['2014-06-16']


# In[11]:


# What are the types and sizes of each of our columns?
df.info()


# ### Why didn't Pandas import all those `police_district` numbers as integers?
# 
# (They are listed as `<object>` above and the first few in `.head()` all look like integers)
# So let's try to manually convert them ourselves

# In[12]:


df.police_district.astype(int)


# In[14]:


# Can we mask out everything except crimes in this nonnumbered police district called "OP"
mask = (df.police_district == 'OP')
df[mask].head()


# In[23]:


# let's clean up that major_offense_type string to make it consistently spelled and capitalized
df.major_offense_type = df.major_offense_type.str.lower().str.strip()
# now let's count them up
df.major_offense_type.value_counts()


# *Looks like gambling is not a popular crime*  
# (or at least not a popular *police reported* crime)  

# In[24]:


# Now let's count up crimes by police district
# Notice any non-integer values?
district_counts = trespasses.police_district.value_counts()
district_counts


# In[25]:


mask = df.major_offense_type == 'trespass'
trespasses = df[mask]
df[mask].describe()


# In[32]:


district_counts


# In[42]:


# let's create a dictionary of all the crime counts in all the districts
dict(zip(district_counts.index, district_counts))


# In[43]:


# Let's talk about dict and zip to make sure you understand the code above
dict([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)])


# In[47]:


# dict will accept any sequences of pairings (2-tuples)
# but what if we have two sequences of values that we want to "pair up"
# zip brings the two sides of a pair (the sides of a zipper) together in an alligned pairing
list(zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))


# In[48]:


# and a dict is can take a list of pairs, like before... so
dict(zip(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))


# In[49]:


# and `range(5)` is a sequence (iterable)
dict(zip(['a', 'b', 'c', 'd', 'e'], range(5)))


# In[50]:


# if we get the length wrong, the zipper will get "stuck" on the shortest sequence
dict(zip(['a', 'b', 'c', 'd', 'e'], range(4)))


# In[51]:


# or because any sequence will do, and a str is a sequence of characters:
dict(zip('abcde', range(5)))


# In[ ]:


# What will happen if you try to coerce a list of 3-tuples into a dict?
dict([('a', 1, 2), ('b', 3, 4)])


# In[42]:


x = list(range(3))
y = list(range(4))
print(x)
print(y)
list(zip(x, y, range(5)))


# In[45]:


x = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
list(zip(*x))


# In[46]:


list(zip(x[0], x[1], x[2]))


# In[78]:


df.report_date = pd.to_datetime(df.report_date)
df.report_date


# In[52]:


def fun(x):
    return str(x)

df.report_date.apply(fun)
# df.


# In[53]:


# df.plot.scatter(x='xcoordinate', y='ycoordinate', c='r')
df.plot(kind='scatter', x='xcoordinate', y='ycoordinate', c='r')

from matplotlib import pyplot as plt
plt.show()


# In[54]:


df.std()


# In[57]:


trespasses.plot(kind='scatter', x='xcoordinate', y='ycoordinate')
plt.show()


# In[79]:


colornums = mask.astype(int)
# print(type(colornums))
# colornums?
# print(colornums.__dict__)
# print(colornums)


# In[80]:


# colornums.index = pd.Series(colornums.index).apply(chr)
colornums


# In[81]:


colors = np.array(['b', 'r'])[colornums]
colors


# In[ ]:





# In[82]:


df.plot(kind='scatter', x='xcoordinate', y='ycoordinate', c=colors)


# In[84]:


plt.show()


# In[86]:


df.sample(100).plot.scatter(x='xcoordinate', y='ycoordinate')


# In[87]:


plt.show()


# In[89]:


df.xcoordinate.hist(bins=20)


# In[91]:


df.ycoordinate.hist(bins=20)
plt.show()


# In[92]:


get_ipython().magic(u'pinfo df.plot')


# In[90]:


plt.show()


# In[93]:


df.plot.density(x='xcoordinate', y='ycoordinate')


# In[95]:


get_ipython().system(u'pip install mpld3')
import mpld3


# In[99]:


df.sample(1000).plot.scatter(x='xcoordinate', y='ycoordinate')
mpld3.enable_notebook()
plt.show()


# In[94]:


plt.show()


# In[ ]:




from sklearn import datasets

iris_dataset = datasets.load_iris()
X = iris_dataset.data
Y = iris_dataset.target

iris_dataframe = pd.DataFrame(X, columns=iris_dataset.feature_names)
# create a scatter matrix from the dataframe, color by y_train
grr = pd.scatter_matrix(iris_dataframe, c=Y, figsize=(15, 15), marker='o',
                        hist_kwds={'bins': 20}, s=60, alpha=.8)

