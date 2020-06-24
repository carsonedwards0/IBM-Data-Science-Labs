#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a


# In[3]:


A = np.array(a)
A


# In[4]:


A.ndim


# In[5]:


A.shape


# In[6]:


A.size


# In[7]:


A[1, 2]


# In[8]:


A[1][2]


# In[9]:


A[0][0]


# In[10]:


A[0][0:2]


# In[11]:


A[0:2, 2]


# In[12]:


X = np.array([[1, 0],[0, 1]])
X


# In[13]:


Y = np.array([[2, 1], [1, 2]])
Y


# In[14]:


Z = X + Y
Z


# In[15]:


Z = 2 * Y
Z


# In[16]:


Y = np.array([[2, 1], [1, 2]])
Y


# In[17]:


X = np.array([[1, 0], [0, 1]])
X


# In[18]:


Z = X * Y
Z


# In[19]:


A = np.array([[0, 1, 1], [1, 0, 1]])
A


# In[20]:


B = np.array([[1, 1], [1, 1], [-1, 1]])
B


# In[21]:


Z = np.dot(A, B)
Z


# In[22]:


np.sin(Z)


# In[23]:


C = np.array([[1, 1], [2, 2], [3, 3]])
C


# In[24]:


C.T


# In[ ]:




