#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 1 TITANIC SURVIVAL
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# load the dataset
data=pd.read_csv("C:\\Users\\chand\\OneDrive\\Desktop\\sundram desktop\\Titanic-Dataset.csv")

data.head()


# In[2]:


#Creating DataFrame
b=pd.DataFrame(data)
b


# In[3]:


#last few rows of your DataFrame
b.tail()


# In[4]:


#descriptive statistics of a DataFrame
b.describe()


# In[5]:


#concise summary of a DataFrame, including information about the data types
b.info()


# In[6]:


#select column from your DataFrame
b[['PassengerId','Ticket']]


# In[7]:


#Indexing and selecting data
b.loc[2,'PassengerId'] # 2=row index


# In[8]:


b.iloc[3,5] # 3= row index ,5=column index


# In[9]:


#Filtering rows based on condition
b[b['Fare']>30]


# In[10]:


# Droping the column
a=b.drop('Sex',axis=1)
a


# In[11]:


# Arranging the position of column
a[['PassengerId','Fare','Ticket','Name','Age']]


# In[12]:


#Variance & standard Devition
a.var()


# In[13]:


a.std()


# In[14]:


#Correlation & Covariance
a.corr()


# In[15]:


a.cov()


# In[ ]:




