#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


class Circle(object):
    
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
        
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


# In[11]:


RedCircle = Circle(10, 'red')


# In[12]:


dir(RedCircle)


# In[13]:


RedCircle.radius


# In[14]:


RedCircle.color


# In[15]:


RedCircle.radius = 1
RedCircle.radius


# In[16]:


RedCircle.drawCircle()


# In[17]:


print('Radius of Object:' , RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):', RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):' , RedCircle.radius)


# In[24]:


BlueCircle = Circle(100, 'blue')


# In[25]:


BlueCircle.radius


# In[27]:


BlueCircle.color


# In[28]:


BlueCircle.drawCircle()


# In[31]:


class Rectangle(object):
    
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color
    
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()


# In[32]:


SkinnyBlueRectangle = Rectangle(2, 10, 'blue')


# In[33]:


SkinnyBlueRectangle.height


# In[34]:


SkinnyBlueRectangle.width


# In[35]:


SkinnyBlueRectangle.color


# In[36]:


SkinnyBlueRectangle.drawRectangle()


# In[40]:


FatYellowRectangle = Rectangle(20, 5, 'yellow')


# In[41]:


FatYellowRectangle.height


# In[42]:


FatYellowRectangle.width


# In[43]:


FatYellowRectangle.color


# In[44]:


FatYellowRectangle.drawRectangle()


# In[ ]:




