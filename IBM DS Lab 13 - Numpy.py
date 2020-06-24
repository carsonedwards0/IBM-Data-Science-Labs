#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import sys
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[45]:


def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=.01)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=.05, color='b', head_length=.01)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    
def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color = 'r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color = 'b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


# In[3]:


a = ["0", 1, "two", "3", 4]


# In[4]:


print("a[0]:", a[0])


# In[6]:


print("a[2]:", a[2])


# In[7]:


a = np.array([0,1,2,3,4])
a


# In[8]:


print("a[0]:", a[0])


# In[9]:


type(a)


# In[10]:


a.dtype


# In[11]:


b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])


# In[12]:


b.dtype


# In[13]:


c = np.array([20, 1, 2, 3 ,4])


# In[14]:


c


# In[15]:


c[0] = 100
c


# In[16]:


c[4] = 0
c


# In[17]:


d = c[1:4]


# In[18]:


d


# In[19]:


c[3:5] = 300, 400
c


# In[20]:


select = [0, 2, 3]


# In[21]:


d = c[select]
d


# In[22]:


c[select] = 100000
c


# In[23]:


a = np.array([0, 1, 2, 3, 4])
a


# In[24]:


a.size


# In[25]:


a.ndim


# In[26]:


a.shape


# In[27]:


a = np.array([1, -1, 1, -1])


# In[30]:


mean = a.mean()


# In[31]:


mean


# In[32]:


standard_deviation = a.std()
standard_deviation


# In[33]:


b = np.array([-1, 2, 3, 4, 5])
b


# In[34]:


max_b = b.max()
max_b


# 

# 

# In[35]:


min_b = b.min()
min_b


# In[36]:


u = np.array([1, 0])
u


# In[37]:


v = np.array([0, 1])
v


# In[38]:


z = u + v


# In[39]:


z


# In[46]:


Plotvec1(u, z, v)


# In[47]:


y = np.array([1, 2])
y


# In[48]:


z = 2 * y
z


# In[49]:


u = np.array([1, 2])
u


# In[50]:


v = np.array([3, 2])
v


# In[51]:


z = u * v
z


# In[52]:


np.dot(u, v)


# In[53]:


u = np.array([1, 2, 3, -1])
u


# In[54]:


u + 1


# In[55]:


np.pi


# In[56]:


x = np.array([0, np.pi/2, np.pi])


# In[57]:


y = np.sin(x)
y


# In[58]:


np.linspace(-2, 2, num=5)


# In[59]:


np.linspace(-2, 2, num=9)


# In[60]:


x = np.linspace(0, 2*np.pi, num=100)


# In[61]:


y = np.sin(x)


# In[62]:


plt.plot(x, y)


# In[63]:


a=np.array([1,1,1,1,1])
a+10 


# In[65]:


a=np.array([1,1,1,1,1])
b=np.array([2,2,2,2,2])
a*b 


# In[ ]:




