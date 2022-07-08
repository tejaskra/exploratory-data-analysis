#!/usr/bin/env python
# coding: utf-8

# ## We have used the employee data for the exploratory data analysis. It contains 8 columns namely – First Name, Gender, Start Date, Last Login, Salary, Bonus%, Senior Management, and Team.

# In[4]:


import pandas as pd


# In[5]:


data=pd.read_csv("employees.csv")


# In[6]:


data


# ## To print the first five rows we will use the head() function.

# In[7]:


data.head()


# ## To print the info of the dataset

# In[18]:


data.info()


# ##  To print the the shape of the data using the shape function.

# In[19]:


data.shape

data.tail()


# ## The describe() function applies basic statistical computations on the dataset like extreme values, count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. describe() function gives a good picture of the distribution of data.

# In[10]:



data.describe()


# ## To find the sum of missing values in each column

# In[20]:



data.isnull().sum()


# ## To fill the missing values of gender with the string “No Gender

# In[22]:


data["Gender"].fillna("No Gender", inplace = True) 
    
data.isnull().sum()


# ## To fill the senior management with the mode value.

# In[26]:



import numpy as np
mode = data['Senior Management'].mode().values[0]
data['Senior Management']= data['Senior Management'].replace(np.nan, mode)
  
data.isnull().sum()


# ## drop all the rows containing these missing values.

# In[27]:


data = data.dropna(axis = 0, how ='any')

print(data.isnull().sum())
data.shape


#  ## Histogram can be used for both uni and bivariate analysis
# 

# In[28]:



import seaborn as sns
import matplotlib.pyplot as plt


sns.histplot(x='Salary', data=data, )
plt.show()


# ## Boxplot can also be used for univariate and bivariate analyses.

# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt
  
  
sns.boxplot( x="Salary", y='Team', data=data, )
plt.show()


# ## Scatter plot can be used for bivariate analyses

# In[30]:



import seaborn as sns
import matplotlib.pyplot as plt


sns.scatterplot( x="Salary", y='Team', data=data,
        hue='Gender', size='Bonus %')

plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()


# In[ ]:




