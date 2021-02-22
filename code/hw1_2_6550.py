#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:20:07 2021

@author: catalina
""" 
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from scipy.stats import weibull_min
import scipy.stats as stats

#Weibull distribution. #alpha(A) = 1 and Beta(B) =
#s = random.weibullvariate(alpha, beta)
#beta=shape parameter 
#alpha= scale parameter
#plt.hist(s)

ns=[]
i_means=[] 
data={} 
names=[]
df = pd.DataFrame(data)
n_means=[]
n_sds=[]
sq_ns=[]
alpha, betha = 1, 1

for n in range(1,51):
    ns.append(n)
    name=str(n)
    names.append(name)
    for i in range(1,1001):
        s = weibull_min.rvs(betha, loc=0, scale=alpha, size=n)
        i_mean = np.mean(s)
        i_means.append(i_mean)
    df[name] = i_means
    plt.hist(i_means, label= 'n={}'.format(n))
    plt.xlabel("Means")
    plt.ylabel("Relative Frequency")
    plt.title("Means of a Weibull distribution using 1000 trials")
    n_mean = np.mean(i_means)
    n_sd = np.std(i_means)
    sq_n = n_sd/(math.sqrt(n))
    sq_ns.append(sq_n)
    i_means=[]
    n_means.append(n_mean)
    n_sds.append(n_sd)

#plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2.png', dpi=300)
print('The mean of the sample means is {}'.format(np.mean(n_means)))

x = np.random.normal(loc=0, scale=1, size =1000)
 
#%%#Plot results 2a.
#n=1
tmeans = df['1']
tmean = np.mean(tmeans)
tsd = np.std(tmeans)
plt.hist(tmeans, label="n=1")
plt.legend(loc='upper right')
plt.xlabel("Weibull floating number")
plt.ylabel("Relative frequency")
plt.title("Sampled distribution over 1000 trials")
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2a.png', dpi=300)
plt.show()

#%%Plot results 2b.

#Plot results 1b.
boxplot = plt.figure();
ax=df.boxplot(widths = 0.6, grid=False, rot=45, fontsize=6)
ax.set_title('Mean of 1000 trials per n')
ax.set_xlabel('n')
ax.set_ylabel('Mean')
boxplot.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2b_1.png', dpi=300)

fig, ax = plt.subplots(constrained_layout=True)
ax.scatter(ns, n_sds, c='orange', label="SD")
ax.legend(loc='upper left')
plt.ylim([0, 1.2])
ax.set_xlabel("n")
ax.set_ylabel("SD")
plt.title("SD for estimated sample mean at sampling size (n)")
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2b.png', dpi=300)
plt.show()

#%%Plot results 2c.

#Plot before transformation n=3
tmeans = df['3']
plt.hist(tmeans, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution before transformation at n=3")

#Testing normality with a Kolmogorov-Smirnov test.
#Normalized vector
plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2c_1.png', dpi=300)
plt.show()
results = pd.DataFrame(columns=['n', 'Mean', 'SD', 'Statistic', 'p-value', 'Reject NH'])
k=0
alpha = 0.05
n=''

for j in names:
    vector = df[j]
    y=stats.zscore(vector) 
    stat, p = stats.ks_2samp(y, x)
    m=np.mean(y)
    sd=np.std(y)
    if p > alpha:
        hn='No'
    else:
        hn='Yes'        
    results.loc[k] = [format(j), format(m), format(sd), format(stat), format(p), hn]
    k=k+1
    n=''
    
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_2c.csv")  
y=[]

#Plot after transformation n=3
tmean3 = df['3']
y=stats.zscore(tmean3)
plt.hist(y, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution after transformation at n=3")
plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2c_2.png', dpi=300)
plt.show()


#%%Plot results 2d.
results = pd.DataFrame(columns=['n', 'Mean', 'SD', 'Statistic', 'p-value', 'Reject NH'])
k=0
alpha = 0.05
n=''

for j in names:
    vector = df[j]
    y=np.log10(vector)
    z=stats.zscore(y)
    stat, p = stats.ks_2samp(z, x)
    m=np.mean(y)
    sd=np.std(y)
    if p > alpha:
        hn='No'
    else:
        hn='Yes'        
    results.loc[k] = [format(j), format(m), format(sd), format(stat), format(p), hn]
    k=k+1
    n=''
       
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_2d.csv")  
y=[] 

#Plot after transformation n=3
tmean3 = df['3']
y=np.log10(tmean3)
plt.hist(y, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Log10 Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution after Log10 transformation at n=3")
plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2d.png', dpi=300)
plt.show()


#%%Plot results 2e.

#Plot before transformation n=20
tmeans = df['20']
plt.hist(tmeans, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution before transformation at n=20")

plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2e_1.png', dpi=300)
plt.show()

#Plot after transformation n=20
tmean3 = df['20']
y=stats.zscore(tmean3)
plt.hist(y, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution after transformation at n=20")
plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2d_e.png', dpi=300)
plt.show()

#%%Plot results 2f.

ns=[]
i_means=[] 
data={} 
names=[]
df = pd.DataFrame(data)
n_means=[]
n_sds=[]
sq_ns=[]
alpha, betha = 10, 2

for n in range(1,51):
    ns.append(n)
    name=str(n)
    names.append(name)
    for i in range(1,1001):
        s = weibull_min.rvs(betha, loc=0, scale=alpha, size=n)
        i_mean = np.mean(s)
        i_means.append(i_mean)
    df[name] = i_means
    plt.hist(i_means, label= 'n={}'.format(n))
    plt.xlabel("Means")
    plt.ylabel("Relative Frequency")
    plt.title("Means of a Weibull distribution using 1000 trials")
    n_mean = np.mean(i_means)
    n_sd = np.std(i_means)
    sq_n = n_sd/(math.sqrt(n))
    sq_ns.append(sq_n)
    i_means=[]
    n_means.append(n_mean)
    n_sds.append(n_sd)

print('The mean of the sample means is {}'.format(np.mean(n_means)))
plt.show()

#x = np.random.normal(loc=0, scale=1, size =1000)


#Plot before transformation n=3
tmeans = df['3']
plt.hist(tmeans, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution before transformation at n=3")

#Testing normality with a Kolmogorov-Smirnov test.
#Normalized vector
plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2f_1.png', dpi=300)
plt.show()
results = pd.DataFrame(columns=['n', 'Mean', 'SD', 'Statistic', 'p-value', 'Reject NH'])
k=0
alpha = 0.05
n=''

for j in names:
    vector = df[j]
    y=stats.zscore(vector) 
    stat, p = stats.ks_2samp(y, x)
    m=np.mean(y)
    sd=np.std(y)
    if p > alpha:
        hn='No'
    else:
        hn='Yes'        
    results.loc[k] = [format(j), format(m), format(sd), format(stat), format(p), hn]
    k=k+1
    n=''
    
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_2f.csv")  
y=[]

#Plot after transformation n=3
tmean3 = df['3']
y=stats.zscore(tmean3)
plt.hist(y, label="Weibull", color= 'orange')
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Means distribution after transformation at n=3")
plt.hist(x, label="Normal std", alpha=0.3)
plt.legend(loc='upper right')
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 2f_2.png', dpi=300)
plt.show()












