#!/usr/bin/env python
# coding: utf-8

# In[1]:


Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


# In[3]:


Dict["key1"]


# In[4]:


Dict[(0, 1)]


# In[5]:


release_year_dict = {"Thriller": "1982", "Back in Black": "1980",                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",                     "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# In[6]:


release_year_dict['Thriller']


# In[7]:


release_year_dict['The Bodyguard']


# In[8]:


release_year_dict.keys()


# In[13]:


release_year_dict['Graduation'] = "2007"


# In[14]:


release_year_dict


# In[15]:


del(release_year_dict["Thriller"])


# In[16]:


release_year_dict


# In[17]:


"The Bodyguard" in release_year_dict


# In[20]:


soundtrack_dict = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dict


# In[21]:


soundtrack_dict.keys()


# In[22]:


soundtrack_dict.values()


# In[24]:


album_sales_dict = {"Back in Black":"50 million", "The Bodyguard":"50 million", "Thriller":"65 million"}


# In[25]:


album_sales_dict


# In[26]:


album_sales_dict.keys()


# In[28]:


album_sales_dict["Thriller"]


# In[29]:


album_sales_dict.values()


# In[ ]:




