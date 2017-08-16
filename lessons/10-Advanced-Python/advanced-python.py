
# coding: utf-8

# In[4]:


import os
# !pip install seaborn


# In[12]:


# Our bot would like to know who's logged into the computer
# Where can we access environment variables
# try `os.e<tab>` or `os?` or `help(os)` to look for an Operating System feature like environment variables
help(os)


# In[13]:


print(os.environ)


# In[14]:


# os.environ is some sort of combination dictionary and environment object
# this is because it is "editable" so you can change your OS environment variables in python!
# but that means you have to get the environment variable names right
os.environ['USERNAME']


# In[21]:


# on dictionaries we can use the `get` method to avoid KeyError's
# `.get` also allows us to set a default value to be returned if the key doesn't exist
print(os.environ.get('USERNAME'))


# In[22]:


print(os.environ.get('USERNAME', 'default'))


# In[23]:


# there's also a convenience function in `os` if you just want to *READ* a variable on an unknown operating system
print(os.getenv('USERNAME'))


# In[5]:


# Our bot would like to know who's logged into the computer
# Where can we access environment variables
print(sorted(os.environ.keys()))


# In[8]:


os.environ['USERNAME']


# In[7]:


# So we could look for the $USER variable
os.environ['USER']


# In[24]:


# we can also check multiple variations and use the first one that isn't None
os.getenv('USERNAME') or os.getenv('USER')


# In[ ]:


# do a [ctrl]-F on your user name to find it among some of your other environment variables
# notice that it is part of your HOME path?
os.path.basedir

