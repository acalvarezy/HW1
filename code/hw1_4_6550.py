#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:28:17 2021

@author: catalina
"""
#H1, H2, H3, ..., Hm -> Hypothesis
#p1, p2, p3, ..., pm -> p-values

import pandas as pd 
import numpy as np
import scipy.stats as stats

    
#%%4a.   
 
p_values = [0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344, 0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.000]
q = 0.05
m = len(p_values)
results = pd.DataFrame(columns=['Position', 'pvalue', 'Cutoff', 'Rejected'])
rj = ''
rjc = 0
x = len(p_values)
z = 1
for i in reversed(range(0, m)):
    rj='No'
    pi = p_values[i]
    cutoff = (x*q)/m
    if pi <= cutoff:
        previo = p_values[i+1]
        rj = 'Yes'
        if z == 1:
            print('We reject all the null hypothesis for the first {}'.format(x), ' p-values in the arrray')
            print('The last value that passes the FDR cutoff was {}'.format(previo))
            z = 2
    results.loc[x] = [x, pi, cutoff, rj]
    x = x-1
 
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_4a.csv")
 
 
 
 #%%4.
#Load p-values of example. In this case (3b), 6 false positives were obtained
p_values_file = pd.read_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_3b.csv", delimiter=';')
p_values = p_values_file.pvalue.to_list()
sorted_pvalues = p_values.sort()
q = 0.05
m = len(p_values)
results = pd.DataFrame(columns=['Position', 'pvalue', 'Cutoff', 'Rejected'])
rj = ''
rjc = 0
x = len(p_values)
z = 1
for i in reversed(range(0, m)):
    rj='No'
    pi = p_values[i]
    cutoff = (x*q)/m
    if pi <= cutoff:
        previo = p_values[i+1]
        rj = 'Yes'
        if z == 1:
            print('We reject all the null hypothesis for the first {}'.format(x), ' p-values in the arrray')
            print('The last value that passes the FDR cutoff was {}'.format(previo))
            z = 2
    results.loc[x] = [x, pi, cutoff, rj]
    x = x-1
    
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_4.csv")
 
 
    