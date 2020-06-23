#!/usr/bin/env python
# coding: utf-8

# In[14]:


def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)


# In[7]:


help(add)


# In[8]:


add(1)


# In[9]:


add(2)


# In[15]:


def Mult(a, b):
    c = a * b
    return(c)


# In[16]:


Mult(2, 3)


# In[17]:


Mult(2.3, 2.6)


# In[19]:


Mult(2, "Jimmy")


# In[20]:


def square(a):
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return(c)


# In[21]:


x = 3
y = square(x)
y


# In[22]:


square(2)


# In[26]:


def MJ():
    print("Michael Jackson")
    
def MJ1():
    print("Michael Jackson")
    return(None)


# In[24]:


MJ()


# In[27]:


MJ1()


# In[28]:


print(MJ())
print(MJ1())


# In[29]:


def con(a, b):
    return(a + b)


# In[31]:


con("This ", "is")


# In[32]:


a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 -1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5
c1


# In[33]:


def isGoodRating(rating = 4):
    if (rating < 7):
        print("this album sucks its rating is", rating)
        
    else:
        print("this album is good its rating is", rating)


# In[34]:


isGoodRating()
isGoodRating(10)


# In[36]:


artist = "Michael Jackson"
def printer1(artist):
    internal_var = artist
    print(artist, "is an artist")
    
printer1(artist)


# In[38]:


artist = "Michael Jackson"

def printer(artist):
    global interval_var
    internal_var= "Whitney Houston"
    print(artist, "is an artist")
    
printer(artist)
printer(internal_var)


# In[39]:


def div(a, b):
    c = a / b
    return(c)


# In[ ]:




