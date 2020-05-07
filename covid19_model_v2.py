# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#data = pd.read_csv('C://Users//Peter Phang//Desktop//total_cases.csv')
data = pd.read_csv('C://Users//Peter Phang//Desktop//covid19_malaysia_total_cases.csv')
#data = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
#data = pd.read_csv('C://Users//Peter Phang//Desktop//MALAYSIA_old_covid19.csv')

data=data['Sum of cases in Malaysia']
#data=data['United States']
data=data.reset_index(drop=False)
data.columns=['Timestep','Total Cases']
print(data)

def my_logistic(t,a,b,c):
    return c / (1 + a*np.exp(-b*t))

p0=np.random.exponential(size=3)
print(p0)

bounds=(0,[100000,3,1000000])

import scipy.optimize as optim
x=np.array(data['Timestep'])
y=np.array(data['Total Cases'])


(a,b,c),cov = optim.curve_fit(my_logistic,x,y,bounds=bounds,p0=p0)
print(a,b,c)




def my_logistic(t):
    return c / (1+a*np.exp(-b*t))


plt.scatter(x,y)
x=np.linspace(0,250)
plt.plot(x,my_logistic(x),'k')
plt.title('Logistic Model vs Actual Observations of Coronavirus Cases in Malaysia')
plt.legend(['Logistic Model', 'Actual data'])
#plt.text(230,100,'R-squared={:.2f}%'.format(R_squared*100)) #{:.2f}= means 2 decimal places for the calculated values
plt.figtext(0.14, 0.04, 'Source: MOH', horizontalalignment='left') 
plt.figtext(0.9, 0.04, '© Peter Phang', horizontalalignment='right') 
#plt.figtext(0.14, 0.04, 'Source: Our World in Data.org', horizontalalignment='left') 
plt.xlabel('Days')
plt.ylabel('# of Confirmed Cases')




