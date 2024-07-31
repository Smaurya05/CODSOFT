#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task 3 IRIS FLOWER CLASSIFICATION
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
c=pd.read_csv("C:\\Users\\chand\\OneDrive\\Desktop\\sundram desktop\\IRIS.csv")
c.head()


# In[2]:


c.tail()


# In[3]:


c.shape


# In[4]:


c.describe()


# In[5]:


# Data Cleaning
c.isna().sum()


# In[6]:


c.fillna(method='bfill')


# In[7]:


c.duplicated()


# In[8]:


c.nunique()


# In[9]:


c.columns


# In[10]:


#Data visualise
plt.plot('sepal_width','sepal_length',data=c)
plt.title('Line plot')
plt.xlabel('sepal_width')
plt.ylabel('sepal_length')
plt.show()


# In[11]:


x=c['petal_length']
plt.title('histogram')
plt.hist(x)


# In[12]:


plt.hist(c['sepal_width'], bins=25, alpha=0.45, color='red')
plt.hist(c['sepal_length'], bins=25, alpha=0.45, color='blue')
plt.hist(c['species'], bins=25, alpha=0.45, color='yellow')
plt.title('Histogram')
plt.show()


# In[13]:


c.boxplot(column='petal_width',grid=False,color='blue')
plt.title('boxplot')


# In[14]:


plt.pie(x,data=c)
plt.title('Pie Chart')
plt.show()


# In[ ]:




