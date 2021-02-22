#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd 
import scipy.stats as stats

#Normal distribution. #mu, sigma = 3, 1
#s = np.random.normal(mu, sigma, n)
#plt.hist(s)

ns=[]
i_means=[] 
data={} 
names=[]
df = pd.DataFrame(data)
n_means=[]
n_sds=[]
sq_ns=[]
mu, sigma = 3, 1

for n in range(1,51):
    ns.append(n)
    name=str(n)
    names.append(name)
    for i in range(1,1001):
        s=np.random.normal(mu, sigma, n)
        i_mean = np.mean(s)
        i_means.append(i_mean)
    df[name] = i_means
    plt.hist(i_means, label= 'n={}'.format(n))
    plt.xlabel("Means")
    plt.ylabel("Relative Frequency")
    plt.title("Means of a Normal distribution using 1000 trials")
    n_mean = np.mean(i_means)
    n_sd = np.std(i_means)
    sq_n = n_sd/(math.sqrt(n))
    sq_ns.append(sq_n)
    i_means=[]
    n_means.append(n_mean)
    n_sds.append(n_sd)

plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 1.png', dpi=300)
print('The mean of the sample means is {}'.format(np.mean(n_means)))

x = np.random.normal(loc=0, scale=1, size =1000)
 
#%%
# plot the distribution of sample means and sd of the samples means
plt.hist(n_means)
plt.xlabel("Mean of means for different sampling sizes (n)")
plt.ylabel("Relative Frequency")
plt.title("Means stimation of a normal distribution")
plt.show()


plt.scatter(ns, n_means, label="Estimated sample mean")
plt.xlabel("Sample mean")
plt.xlabel("n")
plt.legend(loc='upper right')
plt.title("Mean at different sampling size (n)")
plt.show()


#%%
#Plot results 1a.
fig, ax = plt.subplots(constrained_layout=True)
ax.scatter(ns, n_sds, c='orange', label="SD")
ax.legend(loc='upper left')
plt.ylim([0, 1.2])
ax.set_xlabel("n")
ax.set_ylabel("SD")
ax2=ax.twinx()
ax2.scatter(ns, sq_ns, c='blue', label="SD/√n")
ax2.legend(loc='upper right')
ax2.set_ylabel('SD/√n')
plt.ylim([0, 1.2])
plt.title("SD for estimated sample mean at sampling size (n)")
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 1a.png', dpi=300)
plt.show()


#%%
#Plot results 1b.
boxplot = plt.figure();
ax=df.boxplot(widths = 0.6, grid=False, rot=45, fontsize=6)
ax.set_title('Mean of 1000 trials per n')
ax.set_xlabel('n')
ax.set_ylabel('Mean')
boxplot.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 1b.png', dpi=300)


#%%Calcule and plot results 1c -1d
#n=3 #n=20
tmeans = df['20']
plt.hist(tmeans, label="n=20")
plt.legend(loc='upper right')
plt.xlabel("Mean")
plt.ylabel("Relative frequency")
plt.title("Mean of the sampled data points for 1000 trials")
plt.savefig('/Users/catalina/Dropbox/UVA/BME 6550/HMW1/Figure 1c_3.png', dpi=300)
plt.show()


#Testing normality with a Kolmogorov-Smirnov test.
#Normalized vector
results = pd.DataFrame(columns=['n', 'Mean', 'SD', 'Statistic', 'p-value',  'Reject NH'])
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
  
results.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_1c_d.csv")  
y=[]

#%%
#Plot results 1e
results2 = pd.DataFrame(columns=['n', 'Mean', 'SD', 'Statistic', 'p-value',  'Reject NH'])
k2=0
alpha = 0.05
n=''

for j in names:
    y2 = df[j] 
    stat, p = stats.ks_2samp(y2, x)
    m=np.mean(y2)
    sd=np.std(y2)
    if p > alpha:
        hn='No'
    else:
        hn='Yes'        
    results2.loc[k] = [format(j), format(m), format(sd), format(stat), format(p), hn]
    k2=k2+1
 
results2.to_csv("/Users/catalina/Dropbox/UVA/BME 6550/HMW1/results_1e.csv")  
y2=[]


            
        




