#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[7]:


path = r"C:/Users/USER/Documents/Python Tutorials/"
#'r' allows path to be read in as a raw string


# In[11]:


#Shows what files are in the path
file_name=os.listdir(path)


# In[10]:


#Check if there's a folder and create one if there isn't
folder_names =["Text Files", "Image Files", "CSV Files"]
for loop in range(0,3):
    if not os.path.exists(path+folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])
    


# In[12]:


#Read each file and place it into the correct folder
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "CSV Files/" + file):
        shutil.move(path + file, path +"CSV Files/" + file)
    elif ".txt" in file and not os.path.exists(path + "Text Files/" + file):
        shutil.move(path + file, path +"Text Files/" + file)
    elif ".png" in file and not os.path.exists(path + "Image Files/" + file):
        shutil.move(path + file, path +"Image Files/" + file)
    else:
        print("There are files in this path that were not moved!")


# In[ ]:




