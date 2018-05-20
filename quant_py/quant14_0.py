# -*- coding: utf-8 -*-
'''
Created on 2018年5月20日

@author: isld
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

RandomNumber = np.random.choice([1,2,3,4,5], 100, True, p=[0.1, 0.1, 0.3, 0.3, 0.2])
#print ('np.random.choice: ', RandomNumber)
print ('pd.Series(RandomNumber).value_counts() ')
print (pd.Series(RandomNumber).value_counts())

HSRet300 = pd.read_csv(u'../data/014/return300.csv')
print ("data type of HSRet300: ", type(HSRet300))

# 根据数据得到一个概率密度函数，然后用这个函数生成曲线
density = stats.kde.gaussian_kde(HSRet300.iloc[:, 1])
bins = np.arange(-5, 5, 0.02)

plt.subplot(211)
plt.plot(bins, density(bins))
plt.title('沪深300收益率序列的概率密度曲线图')

plt.subplot(212)
plt.plot(bins, density(bins).cumsum())
plt.title('沪深300收益率序列的概率累计分布曲线图')

# gen bernomlli random nummber.
# np.random.binomial(n,p,size)
print('np.random.binomial(100, 0.5, 20)')
print(np.random.binomial(100, 0.5, 50))

# 
print ("100次，0.5概率的伯努利实验，有50次取值为1的概率: ", stats.binom.pmf(50, 100, 0.5))
# 累计概率：
dd = stats.binom.pmf(np.arange(45, 56, 1), 100, 0.5)
print ("100从，0.5概率的伯努利实验，结果为45-55的累计概率： ", dd.sum())
print ("100从，0.5概率的伯努利实验，结果为45-55的累计概率： ", stats.binom.cdf(55,100, 0.5)-stats.binom.cdf(44,100,0.5))


ret = HSRet300.iloc[:, 1]
p_bernom = (len(ret[ret>0])/len(ret))
print ('后续的10个交易日，6次上涨的概率: ', stats.binom.cdf(10,10,p_bernom)-stats.binom.cdf(6,10,p_bernom))


# Normal Distribution, Gaussian Distribution


#plt.show()
