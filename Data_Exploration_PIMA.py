#!/usr/bin/env python
# coding: utf-8

# # Data Exploration

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150


# In[3]:


from google.colab import drive
drive.mount('/content/drive/')


# In[2]:


df = pd.read_csv('pima-indians-diabetes.csv')
df.shape


# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


import seaborn as sns
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


mpl.rcParams['figure.dpi'] = 200
corr = df.select_dtypes(include = ['float64', 'int64']).iloc[:, :].corr()
plt.figure(figsize=(10, 10))
ax = sns.heatmap(corr, vmax=1, square=True)
# ax.set_xticklabels(rotation=30)
plt.xticks(rotation=45)
plt.yticks(rotation=45)


# In[7]:


mpl.rcParams['figure.dpi'] = 250
plt.figure(figsize=(20, 20))
f, axes = plt.subplots(1, 4)
sns.boxplot(y=df["Glucose"], ax=axes[0])
sns.boxplot(y=df["BloodPressure"], ax=axes[1])
sns.boxplot(y=df["BMI"], ax=axes[2])
sns.boxplot(y=df["Age"], ax=axes[3])
plt.subplots_adjust(wspace=1)


# In[12]:


sns.countplot(x = 'BMI', data = df)


# In[42]:


sns.distplot(df[df['BloodPressure'].notnull()]['BloodPressure'], kde=False, bins=50);
#sns.distplot(df['BloodPressure'], kde=False, bins=10);


# In[25]:


df[df['BloodPressure'].notnull()].describe()


# In[44]:


mpl.rcParams['figure.dpi'] = 250
plt.figure(figsize=(100, 100))
df_nona= df[df['BloodPressure'].notnull()]
print(df_nona)
g = sns.pairplot(df_nona[['Glucose', 'BloodPressure']] )


# In[50]:


pd.crosstab(df['Outcome'], df['BloodPressure'], margins=True)


# In[51]:


pd.crosstab(df['Outcome'], df['Glucose'], margins=True)


# In[47]:


pd.crosstab(df['Outcome'], df['BMI'], margins=True)


# In[48]:


pd.crosstab(df['Outcome'], df['Age'], margins=True)


# In[31]:


import math
data = [[0.1, 1000], [0.1, 800]]
x = (0.1,1000)
y = (0.1,800)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print(distance)


# In[ ]:




