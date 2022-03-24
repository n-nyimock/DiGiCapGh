#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.chdir(r'D:\CODING\Python Projects')


# In[2]:


pip install plotly


# In[3]:


import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px


# In[4]:


shootingdata = pd.read_csv('shootings.csv')


# In[16]:


shootingdata.head()


# In[5]:


shootingdata.tail()


# In[18]:


shootingdata.describe()


# In[6]:


shootingdata.shape


# In[21]:


shootingdata.columns


# In[8]:


shootingdata.isnull().sum()


# # Race Counts

# In[9]:


shootingdata['race'].value_counts()


# # Which Race was shot the most

# In[36]:


plt.title('Which race was shot the most')
sns.countplot(data = shootingdata, x = 'race')


# # Shots categorized by Gender

# In[10]:


shot_by_gender = shootingdata.gender.value_counts()
shot_by_gender


# In[38]:


plt.title("Shot by Gender")
plt.pie(shot_by_gender, labels=shot_by_gender.index, autopct='%1.1f%%', startangle=180)


# # Shots Categorized by Age

# In[21]:


shot_by_age = shootingdata.age.value_counts()
shot_by_age


# In[11]:


plt.figure(figsize=(20, 10))
plt.title("Shot by Age")
plt.xlabel('Age')
plt.ylabel('Number of deaths')
plt.hist(shootingdata.age, bins=np.arange(5,100,5), color='purple');


# # Top 10 city with shooting counts

# In[12]:


top10_shot_by_city = shootingdata.city.value_counts().head(10)
top10_shot_by_city


# In[13]:


topcity = shootingdata.city.value_counts().to_frame().reset_index()
topcity.columns = ['City','Count']
topcity = topcity[0:10]


# In[14]:


plt.title('Top 10 city with shooting counts')
plt.xticks(rotation=45)
sns.barplot(data=topcity,x='City',y='Count')


# # Items most of the victims were armed with at the time when police shot them?

# In[15]:


shot_by_arms = shootingdata.arms_category.value_counts()
shot_by_arms


# In[37]:


plt.figure(figsize=(15, 10))
plt.title("Killed by Arms Category")
plt.xlabel('Number of deaths')
plt.ylabel('arms_category')
plt.hist(shootingdata.age, bins=np.arange(5,100,5));
plt.show


# # Was the suspect mentally ill?

# In[39]:


plt.title('Was the shot person mentally ill?')
sns.countplot(data = shootingdata, x = 'signs_of_mental_illness')


# # Manner of death

# In[41]:


plt.title('Manner of Death')
sns.countplot(data = shootingdata, x = 'manner_of_death')


# # Number of suspect trying to flee
# 

# In[43]:


plt.title('Suspect Flee vs Not Flee')
sns.countplot(data = shootingdata, x = 'flee')


# In[46]:


plt.figure(figsize=(10,5))
plt.title('Suspect Flee vs Not Flee')
sns.countplot(data = shootingdata, y = 'arms_category')


# In[ ]:




