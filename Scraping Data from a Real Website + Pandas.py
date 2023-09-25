#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[3]:


url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page =requests.get(url)

soup=BeautifulSoup(page.text, 'html')


# In[4]:


print(soup)


# In[5]:


soup.find('table')


# In[6]:


soup.find_all('table')


# In[7]:


soup.find_all('table')[1]


# In[8]:


table=soup.find_all('table')[1]


# In[9]:


soup.find('table', class_='wikitable sortable')


# In[10]:


print(table)


# First get Headers and Titles 

# In[11]:


soup.find_all('th')


# In[12]:


world_titles=table.find_all('th')


# In[13]:


#loop through world titles
world_table_titles=[title.text for title in world_titles]
print(world_table_titles)


# In[14]:


world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)


# Put the above into a Pandas Data Frame

# In[15]:


import pandas as pd


# In[16]:


#Create Data frame
df=pd.DataFrame(columns=world_table_titles)
df


# In[17]:


column_data=table.find_all('tr')


# In[18]:


for row in column_data:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print(individual_row_data)


# In[24]:


#Get rid of the first row that has no information
for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print(individual_row_data)


# In[19]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    
    
    length=len(df)
    df.loc[length]=individual_row_data


# In[20]:


df


# In[21]:


#Export DataFrame into CSV
df.to_csv(r'C:\Users\USER\Documents\Python Projects\Companies.csv', index=False)


# In[22]:


#Export DataFrame into Excel
df.to_excel(r'C:\Users\USER\Documents\Python Projects\Companies2.xlsx', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




