#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Pandas</center>
# 
# ![](https://pandas.pydata.org/_static/pandas_logo.png)
# 
# 
# ## Installation
# 
# Simply,
# ```
# pip install pandas
# ```
# 
# 
# ## Reading data from a CSV file
# 
# You can read data from a CSV file using the ``read_csv`` function. By default, it assumes that the fields are comma-separated.

# In[52]:


# import pandas
import pandas as pd


# >The `imdb.csv` dataset contains Highest Rated IMDb "Top 1000" Titles.

# In[2]:


# load imdb dataset as pandas dataframe
imdb_df= pd.read_csv('imdb_1000.csv')


# In[3]:


# show first 5 rows of imdb_df
print(imdb_df[:5])


# >The `bikes.csv` dataset contains information about the number of bicycles that used certain bicycle lanes in Montreal in the year 2012.

# In[72]:


# load bikes dataset as pandas dataframe
bikes_df = pd.read_csv("bikes.csv", sep=";", parse_dates=['Date'], dayfirst=True, index_col='Date')


# In[73]:


# show first 3 rows of bikes_df
print(bikes_df[:3])


# ## Selecting columns
# 
# When you read a CSV, you get a kind of object called a DataFrame, which is made up of rows and columns. You get columns out of a DataFrame the same way you get elements out of a dictionary.

# In[6]:


# list columns of imdb_df
print(imdb_df.columns)


# In[7]:


# what are the datatypes of values in columns
print(imdb_df.dtypes)


# In[8]:


# list first 5 movie titles
print(imdb_df.title[:5])


# In[9]:


# show only movie title and genre
print(imdb_df[['title','genre']])


# ## Understanding columns
# 
# On the inside, the type of a column is ``pd.Series`` and pandas Series are internally numpy arrays. If you add ``.values`` to the end of any Series, you'll get its internal **numpy array**.

# In[10]:


# show the type of duration column
type(imdb_df['duration'])


# In[11]:


# show duration values of movies as numpy arrays
print(imdb_df['duration'].values)


# ## Applying functions to columns
# 
# Use `.apply` function to apply any function to each element of a column.

# In[31]:


# convert all the movie titles to uppercase
imdb_df['title'].apply(lambda x: x.upper())


# ## Plotting a column
# 
# Use ``.plot()`` function!

# In[74]:


# plot the bikers travelling to Berri1 over the year
bikes_df['Berri1'].plot()


# In[75]:


# plot all the columns of bikes_df

bikes_df.plot()


# ## Value counts
# 
# Get count of unique values in a particular column/Series.

# In[17]:


# what are the unique genre in imdb_df?
imdb_df['genre'].unique()


# In[18]:


# plotting value counts of unique genres as a bar chart
df= imdb_df['genre'].value_counts()
df.plot.bar()


# In[19]:


# plotting value counts of unique genres as a pie chart
df.plot.pie()


# ## Index
# 
# ### DATAFRAME = COLUMNS + INDEX + ND DATA
# 
# ### SERIES = INDEX + 1-D DATA
# 
# **Index** or (**row labels**) is one of the fundamental data structure of pandas. It can be thought of as an **immutable array** and an **ordered set**.
# 
# > Every row is uniquely identified by its index value.

# In[76]:


# show index of bikes_df
bikes_df.index


# In[78]:


# get row for date 2012-01-01
first = bikes_df.loc["2012-01-01"] 
print(first)


# #### To get row by integer index:
# 
# Use ``.iloc[]`` for purely integer-location based indexing for selection by position.

# In[15]:


# show 11th row of imdb_df using iloc
imdb_df.iloc[10]


# ## Selecting rows where column has a particular value

# In[81]:


# select only those movies where genre is adventure
newdf = imdb_df[imdb_df['genre']=='Adventure']
print(newdf[:5])


# In[84]:


# which genre has highest number of movies with star rating above 8 and duration more than 130 minutes?
genree= (imdb_df['duration' ] > 130) & (imdb_df['star_rating'] >8) 
imdb_df[genree]['genre'].value_counts()    


# ## Adding a new column to DataFrame

# In[86]:


# add a weekday column to bikes_df
bikes_df['weekday'] = bikes_df.index.weekday


# ## Deleting an existing column from DataFrame

# In[87]:


# remove column 'Unnamed: 1' from bikes_df
del bikes_df['Unnamed: 1']


# ## Deleting a row in DataFrame

# In[90]:


# remove row no. 1 from bikes_df

bikes_df.drop(bikes_df.index[0])


# ## Group By
# 
# Any groupby operation involves one of the following operations on the original object. They are −
# 
# - Splitting the Object
# 
# - Applying a function
# 
# - Combining the results
# 
# In many situations, we split the data into sets and we apply some functionality on each subset. In the apply functionality, we can perform the following operations −
# 
# - **Aggregation** − computing a summary statistic
# 
# - **Transformation** − perform some group-specific operation
# 
# - **Filtration** − discarding the data with some condition

# In[91]:


# group imdb_df by movie genres
imdb_df.groupby('genre')


# In[95]:


# get crime movies group
print(imdb_df.groupby('genre').get_group('Crime'))


# In[100]:


# get mean of movie durations for each group
print(imdb_df.groupby('genre').aggregate('mean'))


# In[ ]:


# change duration of all movies in a particular genre to mean duration of the group


# In[ ]:


# drop groups/genres that do not have average movie duration greater than 120.


# In[ ]:


# group weekday wise bikers count


# In[ ]:


# get weekday wise biker count


# In[ ]:


# plot weekday wise biker count for 'Berri1'


# ![](https://memegenerator.net/img/instances/500x/73988569/pythonpandas-is-easy-import-and-go.jpg)
