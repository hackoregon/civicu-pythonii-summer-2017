
# coding: utf-8

# In[2]:


import csv


# writer example 
with open('grid.csv', 'w') as fout:
    foo_writer = csv.writer(foo)
    foo_writer.writerow("A B C D".split())
    for i in range(10):
        foo_writer.writerow("A{i} B{i} C{i} D{i}".format(i=i).split()))

filename = 'food-carbon-footprint.csv'
# reader example
with open('grid.csv') as fin: 
    reader = csv.reader(fin)
    
    # this is how you can grab the first header row out of a csv
    header_row = next(reader)
    
    for row in foo_reader:
        print(row)
   
    


# In[ ]:





# In[2]:


import pandas as pd
df = pd.read_html('http://www.greeneatz.com/foods-carbon-footprint.html', header=0)[0]
df.to_csv('food-carbon-footprint.csv')
df


# In[ ]:





# In[4]:


df.mean()
for i, row in df.iterrows():
    print(row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




