#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import optimize

from plotly.offline import iplot, plot
import plotly
import plotly.graph_objs as go


# In[60]:


data=pd.read_csv("D:\DataScience\Python\Programs\I-learn-Python\machine_learning\learning_on_labeled_data\weights_heights.csv", index_col='Index')
print (data.info())
print (data.head())

print (data.plot(y='Height', kind='hist', color='red', title='Height (inch.) distribution'))
print (data.plot(y='Weight', kind='hist', color='green', title='Weight (pounds) distribution'))


# In[8]:


data['BMI']=data.Weight/((data.Height)**2)*703
print (data.head())
print (sns.pairplot(data))


# In[9]:


weight_category=[]
for elem in data['Weight']:
    if elem < 120:
        weight_category.append(1)
    elif elem >=150:
        weight_category.append(3)
    else:
        weight_category.append(2)
data['weight_category']=weight_category      
print (data.head())
weight_category_and_Height=sns.boxplot(data=data, x='weight_category', y='Height')
weight_category_and_Height.set(ylabel = 'Рост', xlabel = 'Весовая категория')
print (weight_category_and_Height)


# In[10]:


Weight_and_Height=data.plot(kind='scatter', x='Weight', y='Height', title='Зависимость роста от веса')
print (Weight_and_Height)


# In[51]:


def get_y(w0, w1,x):
    return(w0+w1*x)
def get_error(w0,w1):
    return (sum(map(lambda x, y: (y-get_y(w0, w1,x))**2, data['Weight'], data['Height'])))


# In[61]:


def make_model_plot(w_values):
    data.plot(kind='scatter', x='Weight', y='Height', title='Зависимость роста от веса')
    x_range=np.linspace(40,200,100)
    colors=['red', 'orange']
    for w0, w1 in w_values:
        y=list(map(lambda x: get_y(w0, w1,x), x_range))
        color = colors.pop()
        plt.plot(x_range, y,color=color, lw=2)
print (make_model_plot([(60, 0.05), (50, 0.16)]))


# In[57]:


# w0=50
# w1=np.linspace(-5,7,100)
# error=list(map(lambda p: get_error(w0,p), w1))
# plt.plot(w0, w1)


# In[66]:


w0=50
w1_opt=optimize.minimize_scalar(lambda x: get_error(w0,x), [-5,5]).x
print (w1_opt)
make_model_plot([(w0, w1_opt)])


# In[71]:


def get_error_opt(w):
    return get_error(w[0], w[1])

w0_opt, w1_opt = optimize.minimize(get_error_opt, (0,0), bounds = [(-100, 100), (-5, 5)], method = 'L-BFGS-B').x
print (w0_opt, w1_opt)
make_model_plot([(w0_opt, w1_opt)])

