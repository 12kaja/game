#!/usr/bin/env python
# coding: utf-8

# # EDA Project On IPL Data Set

# In[2]:


import pandas as pd
import numpy as np
from  import pyplot as plt
import seamatplotlibborn as sns


# In[3]:


#read data
df=pd.read_csv("matches.csv")
df


# In[7]:


# show five record of the dataset

df.head()


# In[5]:


#show NO.Of row and column in data set

df.shape


# In[6]:


#find null value
#veriable=pd.isnull(old data name['column name'])
bool_series = pd.isnull(df["umpire1"])
df[bool_series]


# In[7]:


#getting the frequency of most man of the match award

df['player_of_match'].value_counts()


# In[9]:


#getting the top 10 player which most man of the match award

df['player_of_match'].value_counts()[0:10]


# In[10]:


list(df['player_of_match'].value_counts()[0:5].keys())


# In[11]:


#show highest match wich city

fig_dims=(30,4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='city',ax=ax,data=df)
plt.show()


# In[44]:


#show highest match wich season

fig_dims=(20,4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='season',ax=ax,data=df)
plt.show()


# In[41]:


# most successful IPL team

df1=df.winner.value_counts()
sns.lineplot(y=df1.index,x=df1)


# In[14]:


#making bar plot for the 5 player with most of the match aword

plt.figure(figsize=(8,5))
plt.bar(list(df['player_of_match'].value_counts()[0:5].keys()),list(df['player_of_match'].value_counts()[0:5]),color='g')
plt.show()


# In[15]:


#getting the frequency of result column

df['result'].value_counts()


# In[16]:


#finding out the no.of toss wins w.r.t each team

df['toss_winner'].value_counts()


# In[ ]:





# In[17]:


#extracting the record where a team won batting first

batting_first=df[df['win_by_runs']!=0]


# In[18]:


batting_first.head()


# In[19]:


#making a histogram

plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.title('Distribution Of Runs')
plt.xlabel('Runs')
plt.show()


# In[20]:


#finding out the no.of  wins w.r.t each team after batting first

batting_first['winner'].value_counts()


# In[21]:


#making bar plot for the 5  most win after batting first 

plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=['blue','yellow','orange'])
plt.show()


# In[22]:


# making a Pie chart

plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.title('Winner Of First Batting')
plt.show()


# In[23]:


#finding out the no.of  wins w.r.t each team after batting secomd

batting_second=df[df['win_by_wickets']!=0]
batting_second.head()


# In[24]:


#making a histogram for frequency of wins number of wickets

plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.title("Second Batting Win Match")
plt.xlabel('Wickets')
plt.show()


# In[25]:


batting_second['winner'].value_counts()


# In[26]:


#making bar plot for the 3  most win after batting second

plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=['purple','blue','red'])
plt.show()


# In[27]:


# making a Pie chart

plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.title('Winner Of Second Batting')
plt.show()


# In[28]:


# no.of maches played each season

df['season'].value_counts()


# In[29]:


#looking at the no.of maches played in each city 
df['city'].value_counts()


# In[17]:


#finding how many time a team has won match after winig the toss

np.sum(df['toss_winner']==df['winner'])


# In[31]:


325/636


# In[32]:


data=pd.read_csv('Deliveries IPL 2008-2019.csv')
data.head()


# In[33]:


match_1=data[data['match_id']==1]
match_1


# In[34]:


match_1.shape


# In[35]:


srh=match_1[match_1['inning']==1]
srh.head()


# In[36]:


srh['batsman_runs'].value_counts()


# In[37]:


srh['dismissal_kind'].value_counts()


# In[38]:


rcb=match_1[match_1['inning']==2]
rcb.head()


# In[39]:


rcb['batsman_runs'].value_counts()


# In[40]:


rcb['dismissal_kind'].value_counts()


# In[ ]:





# In[ ]:




