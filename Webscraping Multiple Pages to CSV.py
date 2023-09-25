#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[6]:


#Turn the above into html code that you can access
#To do so, use Beautiful Soup
from bs4 import BeautifulSoup


# In[24]:


import pandas as pd


# In[26]:


books=[] #Define a list of books in an empty list and add below infrmation to it
for i in range(1,51):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"
    response=requests.get(url)
    response=response.content
    soup=BeautifulSoup(response, 'html.parser')
    ol=soup.find('ol')
    articles=ol.find_all('article',class_='product_pod' )



    #Loop through article to get the title, star rating and price
    for article in articles: 
        image=article.find('img') #find the image tag
        title=image.attrs['alt'] #Get attributes of that title
        star=article.find('p') #Get star ratings
        star=star['class'][1]
        price=article.find('p', class_='price_color').text #To only get the price and not additional things
        price=float(price[1:]) #we only want the price with no currency sign and convert it to a float so that we can do calculations
        books.append([title, price, star])



# In[27]:


df=pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating'])


# In[32]:


#Turn the DataFrame into a csv filed and name it 'Books.csv'
df.to_csv(r'C:\Users\USER\Documents\Python Projects\Books.csv', index=False)


# In[34]:


#Turn to MS Excel
df.to_excel(r'C:\Users\USER\Documents\Python Projects\Books.xlsx', index=False)


# In[35]:


#Call the DataFrame to see what it looks like
df


# In[ ]:




