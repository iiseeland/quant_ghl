
'''
Created on 2018年5月20日

# -*- coding: utf-8 -*-
@author: isld
'''
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


returns = pd.read_csv(u'../data/013/retdata.csv')

gsyh = returns.gsyh
print (gsyh)
plt.hist(gsyh)
plt.title(u"工商银行收益率")

# 算数平均数
print ('mean of 中国联通', returns.zglt.mean())
print ('mean of 浦发银行', returns.pfyh.mean())

# 中位数
print ('median of 中国联通', returns.zglt.median())
print ('median of 浦发银行', returns.pfyh.median())

# 求众数
print ('mode fo 中国联通', returns.zglt.mode())
print ('mode of 浦发银行', returns.pfyh.mode())


# 百分位数
print ('quantile of 中国联通', [returns.zglt.quantile(i) for i in [0.25, 0.5, 0.75]])
print ('quantile of 浦发银行', [returns.pfyh.quantile(i/100) for i in range(10, 100, 10)])

# 极差
print ("Range of 中国联通", returns.zglt.max() - returns.zglt.min())
# 平均绝对差：
print ('MAD of 中国联通', returns.zglt.mad())
# 方差
print ('Var of 中国联通', returns.zglt.var())
# 标准差
print ('std of 中国联通', returns.zglt.std())









# plt.show()
