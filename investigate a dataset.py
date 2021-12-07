#!/usr/bin/env python
# coding: utf-8

# >Welcome to the Investigate a Dataset project! 
# In it we perform some basic analytic operation on data of movies and conclude some relation between it's parameters 
# 
# # Project:TMBD Movie Data 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# >This data set contains information about 10,000 movies collected from The Movie Database (TMDb),Here we have some interesting data to some operation include maintaining and cleaning to finially have some valuable data , and this depend on the questios we ask like :
# 1- Which genres are most popular from year to year?
# 2-What kinds of properties are associated with movies that have high revenues?
# 

# In[1]:


import numpy as pd 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns  


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.
# 
# ### General Properties

# In[2]:


df = pd.read_csv('tmdb-movies (1).csv')
df.head(5)


# In[3]:


df.shape 


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.drop(['homepage','tagline', 'production_companies'] , axis = 1, inplace = True )


# In[7]:


df.head(3)


# In[8]:


df.hist(figsize=(15,15));


# In[9]:


df[df.cast.isnull()].hist(figsize=(15,15));


# In[10]:


df.fillna(df.mean(), inplace = True)
df.info()


# In[11]:


df.dropna(inplace = True)
df.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > Now we trimmed and cleaned the data, moving on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that we posed in the Introduction section. looking for relationships between variables.
# 

# <a id='eda'></a>
# ### The answer for the first question :

# In[12]:


Genres1 = df.genres == "Action"


# In[13]:


df.release_year[Genres1]


# In[14]:


Genres2 = df.genres == "Adventure"


# In[15]:


df.release_year[Genres2]


# In[16]:


Genres3 = df.genres == "Crime"


# In[17]:


df.release_year[Genres3]


# In[18]:


df.release_year[Genres1].hist(figsize=(10,10), alpha= 0.5, label='Action' );
df.release_year[Genres2].hist(alpha= 0.5, label='Adventure');
df.release_year[Genres3].hist(alpha= 0.5, label='Crime');
plt.legend();


# ### The answer for the second question :

# In[26]:


df.groupby('revenue').vote_average.mean().plot(kind='bar',figsize=(15,15));


# <a id='conclusions'></a>
# ## Conclusions
# > Here we reach at the the end of this report which have involved :
# (1)the description of data  ;
# (2)the information about it's fields ;
# (3)visulazing them ; 
# (4)cleaning undesirable data ;
# (5)finding relation between parameters 
