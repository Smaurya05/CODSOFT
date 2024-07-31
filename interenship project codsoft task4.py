#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task4 SALES PREDICTION 

import pandas as pd
# load the dataset
data=pd.read_csv('C:\\Users\\chand\\OneDrive\\Desktop\\sundram desktop\\advertising.csv')

data.head()


# In[2]:


#Creating DataFrame
import numpy as np
b=pd.DataFrame(data)
b


# In[3]:


# First few rows of your DataFrame
b.head()


# In[4]:


#Last few rows of your DataFrame
b.tail()


# In[5]:


#descriptive statitic of DataFrame
b.describe()


# In[6]:


#concies summary of a DataFrame, including information about the data types
b.info()


# In[7]:


#Data visualise
import seaborn as sns
import matplotlib.pyplot as plt
#histogram
sns.histplot(x='Sales', data=b)
plt.title('Histogram')
plt.show()

#boxplot
sns.boxplot( x='Radio', y='TV', data=data )
plt.title('Boxplot')
plt.show()


# In[8]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#prepare the data
x=data[['TV','Radio','Newspaper']]
y=data['Sales']

#split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# choose a madel
model=LinearRegression()

# train the model
model.fit(x_train,y_train)

# make sales predection
y_pred=model.predict(x_test)

#Evaluate the model
mse= mean_squared_error(y_test,y_pred)
print("mean squared error:",mse)

#display actual and predicted sales values
sales_comparison=pd.DataFrame({'Actual sales':y_test,'predicted sales':y_pred})
print(sales_comparison)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




