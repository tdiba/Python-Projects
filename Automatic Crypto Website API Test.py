#!/usr/bin/env python
# coding: utf-8

# In[2]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'fe56484e-e6b0-4962-89b7-8f6fa69bf2e1',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[3]:


type(data)


# In[4]:


import pandas as pd

pd.set_option('display.max_columns', None)


# In[5]:


df=pd.json_normalize(data['data'])

#Add column so that you know exact time it ran
df['timestamp']=pd.to_datetime('now', utc=True)
df


# In[6]:


#Automate process to keep adding dat ato the dataframe

#first create function to run API

def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'fe56484e-e6b0-4962-89b7-8f6fa69bf2e1',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df2=pd.json_normalize(data['data'])
    df2['timestamp']=pd.to_datetime('now', utc=True)
    df=df2.append(df2)
    
    if not os.path.isfile(r'C:\Users\USER\Documents\Python Projects\API\API_Project.csv'):
        df.to_csv(r'C:\Users\USER\Documents\Python Projects\API\API_Project.csv', header='column_names')


# In[7]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60) #sleep for 1 minute
exit()


# In[8]:


df


# In[9]:


#Remove scientific notation in the numbers
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[10]:


df


# In[11]:


#Look at the coin trends over time

df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[13]:


#group all the 
df4 = df3.stack()
df4


# In[14]:


type(df4)


# In[15]:


df5 = df4.to_frame(name='values')
df5


# In[21]:


type(df5)


# In[22]:


df5.count()


# In[28]:


#Because of how it's structured above we need to set an index. We don't want to pass a column as an index for this dataframe
#So we're going to create a range and pass that as the dataframe. 
#You can make this more dynamic, but we're just going to hard code it


index = pd.Index(range(90))

# Set the above DataFrame index object as the index
# using set_index() function
df6 = df5.reset_index()
df6

# If it only has the index and values try doing reset_index like "df5.reset_index()"


# In[29]:


# Change the column name

df7 = df6.rename(columns={'level_1': 'percent_change'})
df7


# In[36]:


df7['percent_change']=df7['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'],['1h', '24h', '7d', '30d', '60d', '90d'])
df7


# In[34]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[37]:


sns.catplot(x='percent_change', y='values', hue='name', data=df7, kind='point')


# In[40]:


# we are going to create a dataframe with the columns we want

df10 = df[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Litecoin'")
df10


# In[41]:


sns.set_theme(style="darkgrid")

sns.lineplot(x='timestamp', y='quote.USD.price', data = df10)


# In[ ]:




