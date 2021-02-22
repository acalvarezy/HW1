#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:19:27 2021

@author: catalina
"""

import numpy as np
import pandas as pd 
import scipy.stats as stats


#%%3a

miu1 = 1
sigma1 = 1
miu2 = 3
sigma2 =1
n = 3

data1 = pd.DataFrame(columns=['trial', 'Mean distribution1', 'Mean distribution1', 't-stat', 'p-value', 'FN'])
alpha = 0.05
fnc = 0

for i in range(1,101):
    d1 = np.random.normal(miu1, sigma1, n)
    mean_d1 =  np.mean(d1)
    d2 = np.random.normal(miu2, sigma2, n)
    mean_d2=np.mean(d2)
    stat, p = stats.ttest_ind(d1, d2)
    if p > alpha:
        fn='Yes'
        fnc=fnc+1 
    else:
        fn='No'
    data1.loc[i] = [i, mean_d1, mean_d2, stat, p, fnc]
    
print('The total number of false negatives is {}'.format(fnc))
data1.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_3a.csv")


#%%3b.

miu1 = 1
sigma1 = 1
miu2 = 1
sigma2 =1
n = 3

data1 = pd.DataFrame(columns=['trial', 'Mean distribution1', 'Mean distribution', 't-stat', 'p-value', 'FP'])
alpha = 0.05
fpc = 0

for i in range(1,101):
    d1 = np.random.normal(miu1, sigma1, n)
    mean_d1 =  np.mean(d1)
    d2 = np.random.normal(miu2, sigma2, n)
    mean_d2=np.mean(d2)
    stat, p = stats.ttest_ind(d1, d2)
    if p > alpha:
        fp='No'
    else:
        fp='Yes'
        fpc=fpc+1 
    data1.loc[i] = [i, mean_d1, mean_d2, stat, p, fp]
    
print('The total number of false positives is {}'.format(fpc))
data1.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_3b.csv")


#%%3c.
miu1 = 1
sigma1 = 1
miu2 = 1
sigma2 =1
n = 3

data1 = pd.DataFrame(columns=['trial', 'Mean distribution1', 'Mean distribution1', 't-stat', 'p-value', 'FP'])
alpha = 0.05
fpc = 0

for i in range(1,1001):
    d1 = np.random.normal(miu1, sigma1, n)
    mean_d1 =  np.mean(d1)
    d2 = np.random.normal(miu2, sigma2, n)
    mean_d2=np.mean(d2)
    stat, p = stats.ttest_ind(d1, d2)
    if p > alpha:
        fp='No'
    else:
        fp='Yes'
        fpc=fpc+1 
    data1.loc[i] = [i, mean_d1, mean_d2, stat, p, fpc]
    
print('The total number of false positives is {}'.format(fpc))
data1.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_3c.csv")


#%%3d.

miu1 = 3
sigma1 = 1
miu2 = 1
sigma2 =1
alpha = 0.05
data1 = pd.DataFrame(columns=['n', 'False Negatives'])

for n in range(1,31):    
    fnc = 0
    for i in range(1,101):
        d1 = np.random.normal(miu1, sigma1, n)
        mean_d1 =  np.mean(d1)
        d2 = np.random.normal(miu2, sigma2, n)
        mean_d2=np.mean(d2)
        stat, p = stats.ttest_ind(d1, d2, )
        if p > alpha:
            fn='Yes'
            fnc=fnc+1 
        else:
            fn='No'
    data1.loc[n] = [n, fnc]

miu1 = 1
sigma1 = 1
miu2 = 1
sigma2 =1
alpha = 0.05
data2 = pd.DataFrame(columns=['n', 'False positives'])

for n in range(1,31):    
    fpc = 0
    for i in range(1,101):
        d1 = np.random.normal(miu1, sigma1, n)
        mean_d1 =  np.mean(d1)
        d2 = np.random.normal(miu2, sigma2, n)
        mean_d2=np.mean(d2)
        stat, p = stats.ttest_ind(d1, d2)
        if p > alpha:
            fp='No'
        else:
            fp='Yes'
            fpc=fpc+1 
    data2.loc[n] = [n, fpc]

results = pd.concat([data1, data2], axis=1)
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_3d.csv")


#%%3e.

miu1 = 1
sigma1 = 2
miu2 = 2
sigma2 = 1
n = 3

data1 = pd.DataFrame(columns=['trial', 'Mean distribution1', 'Mean distribution1', 't-stat', 'p-value', 'FN'])
alpha = 0.05
fnc = 0

for i in range(1,101):
    d1 = np.random.normal(miu1, sigma1, n)
    mean_d1 =  np.mean(d1)
    d2 = np.random.normal(miu2, sigma2, n)
    mean_d2=np.mean(d2)
    stat, p = stats.ttest_ind(d1, d2)
    if p > alpha:
        fn='Yes'
        fnc=fnc+1 
    else:
        fn='No'
    data1.loc[i] = [i, mean_d1, mean_d2, stat, p, fnc]
    
print('The total number of false negatives is {}'.format(fnc))
data1.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_3e_2.csv")




















