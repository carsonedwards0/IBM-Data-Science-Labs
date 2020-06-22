#!/usr/bin/env python
# coding: utf-8

# In[1]:


set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# In[2]:


set1.add("NSYNC")


# In[3]:


set1


# In[4]:


set1.add("NSYNC")


# In[5]:


set1


# In[6]:


set1.remove("NSYNC")


# In[7]:


set1


# In[8]:


"NSYNC" in set1


# In[10]:


album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set1, album_set2

intersection = album_set1 & album_set2
print(intersection
# In[12]:


album_set1.difference(album_set2)


# In[13]:


album_set1.intersection(album_set2)


# In[14]:


set(album_set2).issubset(album_set1)


# In[16]:


set({'rap', 'house', 'electronic music', 'rap'})


# In[17]:


A = [1,2,2,1]
B = set([1,2,2,1])


# In[18]:


sum(A)


# In[19]:


sum(B)


# In[21]:


album_set3 = album_set1.union(album_set2)


# In[22]:


album_set3


# In[23]:


album_set1.issubset(album_set3)


# In[ ]:




