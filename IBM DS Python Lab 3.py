#!/usr/bin/env python
# coding: utf-8

# In[1]:


tuple1 = ("disco", 10, 1.2)
tuple1


# In[2]:


type(tuple1)


# In[5]:


print(type(tuple1[0]))


# In[6]:


print(type(tuple1[1]))


# In[7]:


print(type(tuple1[2]))


# In[8]:


tuple1[-1]


# In[9]:


tuple1[-2]


# In[10]:


tuple1[-3]


# In[11]:


tuple2 = tuple1 + ("hard rock", 10)


# In[12]:


tuple2


# In[13]:


tuple2[0:2]


# In[14]:


tuple2[0:3]


# In[15]:


len(tuple2)


# In[16]:


Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)


# In[17]:


RatingsSorted = sorted(Ratings)


# In[18]:


RatingsSorted


# In[19]:


NestedT = (1, 2, ("pop", "rock") ,(3,4), ("disco", (1,2)))


# In[20]:


NestedT


# In[21]:


print(NestedT)


# In[22]:


print("Element 1 of Tuple: ", NestedT[0])


# In[24]:


print("Element 2 of Tuple: ", NestedT[2])


# In[26]:


genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",                 "R&B", "progressive rock", "disco")
genres_tuple


# In[27]:


len(genres_tuple)


# In[28]:


print(genres_tuple[2])


# In[29]:


genres_tuple[3]


# In[31]:


genres_tuple[3:6]


# In[35]:


genres_tuple[0:2]


# In[38]:


genres_tuple.index("disco")


# In[39]:


C_tuple = (-5, 1, -3)
C_tuple


# In[42]:


C_list = sorted(C_tuple)


# In[43]:


C_list


# In[ ]:




