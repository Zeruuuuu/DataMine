#!/usr/bin/env python
# coding: utf-8

# # Project 9 -- Zeru Zhou

# **TA Help:** NA
# 
# 
#     
# **Collaboration:** NA
#     
# - Get help from Dr. Ward's videos

# ## Question 1

# In[1]:


import pandas as pd


# In[2]:


dat = pd.read_parquet("/depot/datamine/data/disney/total.parquet")
dat.head()


# In[3]:


dat['status'].isna().value_counts()


# In[4]:


dat.groupby("ride_name")['status'].count()


# Number of rows for each rides are listed above.

# ## Question 2

# In[5]:


print(f"There are {dat['SPOSTMIN'].notna().sum()} rows that SPOSTMIN is not null")


# In[6]:


print(f"There are {dat['SACTMIN'].notna().sum()} rows that SACTMIN is not null")


# In[7]:


def sort_combine(dat):
    # Find the time before and after
    dat['time_after']=dat['datetime'].shift(-1)
    dat['time_before']=dat['datetime'].shift(1)
    
    # Find the SPOSTMIN before and after value
    dat['SPOSTMIN_after']=dat['SPOSTMIN'].shift(-1)
    dat['SPOSTMIN_before']=dat['SPOSTMIN'].shift(1)
    
    # Find the time difference
    dat['time_diff_after']=dat['datetime']-dat['time_after']
    dat['time_diff_before']=dat['datetime']-dat['time_before']
    
    # Find the shortest time
    dat['Previous_is_shorter'] = dat['time_diff_after'].abs()>dat['time_diff_before'].abs()
    
    # Filter the NA value
    dat = dat.loc[dat['SACTMIN'].notna(), :]
    
    # Replace value
    dat.loc[dat['Previous_is_shorter']==True, 'SPOSTMIN'] = dat.loc[dat['Previous_is_shorter']==True, 'SPOSTMIN_before']
    dat.loc[dat['Previous_is_shorter']!=True, 'SPOSTMIN'] = dat.loc[dat['Previous_is_shorter']!=True, 'SPOSTMIN_after']
    
    # Time difference
    dat.loc[dat['Previous_is_shorter']==True, 'time_diff'] = dat.loc[dat['Previous_is_shorter']==True, 'time_diff_before']
    dat.loc[dat['Previous_is_shorter']!=True, 'time_diff'] = dat.loc[dat['Previous_is_shorter']!=True, 'time_diff_after']
    
    # Drop Variables
    dat = dat.drop(columns = ['time_after', 'time_before', 'SPOSTMIN_after', 'SPOSTMIN_before', 'time_diff_after', 'time_diff_before', 'Previous_is_shorter'])
    
    # Return data
    return(dat)
    


# In[8]:


reduced = dat.groupby('ride_name').apply(sort_combine).reset_index(drop=True)
reduced.head()


# New dataframe and columns are created.

# ## Question 3

# In[9]:


reduced.shape


# In[10]:


dat.shape


# In[11]:


3443445-96171


# In[12]:


reduced.groupby('ride_name').median().sort_values('SACTMIN', ascending=True)


# In[13]:


reduced.groupby('ride_name')['SPOSTMIN'].median().plot.bar()


# Reduced dataframe is 3347274 rows less than the original one. The median is closer in compare to the original one. It is close enough to be able to draw compariations because we could see that the time differences are at most few minutes.

# ## Question 4

# In[20]:


reduced = reduced.loc[reduced['time_diff'].abs() <= '0 days 01:00:00']
reduced.shape


# In[21]:


reduced['SPOSTMIN_is_greater']=reduced['SPOSTMIN']>reduced['SACTMIN']


# In[23]:


Count = reduced.groupby('ride_name')['SPOSTMIN_is_greater'].value_counts()


# In[24]:


Count.plot.bar()


# Question: For different ride names, how many of rows are the SPOSTMIN greater than SACTMIN? Hypothesis: In most cases SPOSTMIN would be greater than SACTMIN. The graph is drawn above, and we found that indeed in most cases, SPOSTMINs are greater than  SACTMINs.

# ## Pledge
# 
# By submitting this work I hereby pledge that this is my own, personal work. I've acknowledged in the designated place at the top of this file all sources that I used to complete said work, including but not limited to: online resources, books, and electronic communications. I've noted all collaboration with fellow students and/or TA's. I did not copy or plagiarize another's work.
# 
# > As a Boilermaker pursuing academic excellence, I pledge to be honest and true in all that I do. Accountable together – We are Purdue.
