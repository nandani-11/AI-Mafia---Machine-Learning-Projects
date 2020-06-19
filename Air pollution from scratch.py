#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("./Training Data/Train.csv")
one_arr = np.ones((df.shape[0],))


# In[3]:


x = np.c_[one_arr, df['feature_1'], df['feature_2'], df['feature_3'],  df['feature_4'], df['feature_5']]


# In[4]:


x


# In[5]:


y = df['target'].values
y = y.reshape((-1,))


# In[6]:


def hypothesis(x,theta):
    return np.dot(x,theta)


# In[7]:


def error(x,theta,y):
    err = 0.0
    m = x.shape[0]
    
    for i in range(m):
        hx = hypothesis(x[i],theta)
        err += (hx-y[i])**2
        
    return err


# In[8]:


def gradient(x,theta,y):
    m = x.shape[0]
    
    grad = np.zeros((theta.shape))
    
    for i in range(m):
        hx = hypothesis(x[i],theta)
        
        grad += (hx - y[i])*x[i]
        
    return grad/m


# In[9]:


def gradient_descent(x,y,learning_rate = 0.01):
    
    
    theta = np.zeros((x.shape[1],))
    
    err_list = []
    theta_list = []
    
    
    for i in range(1000):
        grad = gradient(x,theta,y)
        err = error(x,theta,y)
        
        err_list.append(err)
        theta_list.append(theta)
        
        
        theta -= (learning_rate*(grad))
        
    
    return theta,err_list,theta_list


# In[10]:


final_theta , err_list , theta_list = gradient_descent(x,y)


# In[11]:


plt.plot(err_list)


# In[12]:


print(final_theta)


# In[ ]:




