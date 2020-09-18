#!/usr/bin/env python
# coding: utf-8

# # Covid-19 Spread in India

# In[1]:


# Importing necessary libraries 

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


# In[2]:


# Importing the csv files needed

df=pd.read_csv('compare.csv')

dfa=pd.read_csv('countries-aggregated.csv')


# In[3]:


# Visualizing covid cases all over the world

fig=px.choropleth(dfa,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date',color_continuous_scale='OrRd')
fig.show()


# # Comparing confirmed cases and Confirmed rate in India per day

# In[4]:


df_india=df[df['Country']=="India"]
df_india=df_india[['Date','Confirmed']]
df_india['Confirmed Rate']=df_india['Confirmed'].diff()
px.line(df_india,x='Date',y=['Confirmed','Confirmed Rate'],title="Confirmed vs Confirmed rate in India")


# # Comapring status in India before and after lockdown

# ### By the Government of India the lockdown was imposed in 4 phases:-
# 
# Phase 1: 25 March 2020 – 14 April 2020 (21 days)
# 
# Phase 2: 15 April 2020 – 3 May 2020 (19 days)
# 
# Phase 3: 4 May 2020 – 17 May 2020 (14 days)
# 
# Phase 4: 18 May 2020 – 31 May 2020 (14 days)
# 
# ### After the lockdown the Government regulated an Unclock with certain rules and regulations.
# 
# Unlock 1.0: 1 June 2020 – 30 June 2020 (30 days)
# 
# Unlock 2.0: 1 July 2020 – 31 July 2020 (31 days)
# 
# Unlock 3.0: 1 August 2020 – 31 August 2020 (31 days)
# 
# Unlock 4.0: 1 September 2020 - 30 September 2020 (15 days)

# In[5]:


# Initializing the variables

india_lockdown_start_date='14-04-2020'
india_lockdown_end_date='31-05-2020'
india_one_month_after_lockdown='31-06-2020'


# In[6]:


# Representing the graph comparing Before and After lockdown

fig=px.line(df_india,x='Date',y='Confirmed Rate',title="Before and after lockdown")
fig.add_shape(
    dict(
    type="line",
    x0=india_lockdown_start_date,
    y0=0,
    x1=india_lockdown_start_date,
    y1=df_india['Confirmed Rate'].max(),
    line=dict(color="Red")
    ))
fig.add_annotation(
dict(
x=india_lockdown_start_date,
y=df_india['Confirmed Rate'].max(),
text="Starting date of lockdown"
))
fig.add_shape(
    dict(
    type="line",
    x0=india_lockdown_end_date,
    y0=0,
    x1=india_lockdown_end_date,
    y1=df_india['Confirmed Rate'].max(),
    line=dict(color="Orange")
    ))
fig.add_annotation(
dict(
x=india_lockdown_end_date,
y=df_india['Confirmed Rate'].max(),
text="Ending date of lockdown"
))

fig.show()


# #### From this we can see that the lockdown did not have any affect on the rise of covid cases.

# # Comparing in terms of Death rates

# In[7]:


df_india=df[df['Country']=="India"]
df_india["Death rate"]=df_india['Deaths'].diff()
df_india['Confirmed Rate']=df_india['Confirmed'].diff()
df_india


# ## First plotting normal graph without Normalising

# In[8]:


fig=px.line(df_india,x="Date",y=['Death rate','Confirmed Rate'])
fig.show()


# # Graph after normalising the data

# In[9]:


df_india['Death rate']=df_india['Death rate']/df_india['Death rate'].max()
df_india['Confirmed Rate']=df_india['Confirmed Rate']/df_india['Confirmed Rate'].max()
px.line(df_india,x='Date',y=['Death rate','Confirmed Rate'])


# In[ ]:




