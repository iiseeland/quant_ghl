# -*- coding: utf-8 -*-
'''
Created on 2018年5月10日

@author: isld
'''

import numpy as np
import pandas as pd

'''
Series 之间是index匹配运算
Series 跟 DataFrame 之间是 Series跟每一行DataFrame进行匹配（column匹配）运算
DataFrame 之间则是index和cloumn匹配
不匹配的项以 NaN填充
'''

s1 = pd.Series(np.array([1,2,3]), index = list('ABC'))
s2 = pd.Series([4,5,6], index = list('BCD'))
print ("s1+s2 ==> \n", s1+s2, sep = "")

df1 = pd.DataFrame(np.arange(1,13).reshape(3,4), index=list('abc'), columns=list('ABCD'))
print ("df1 - s1 ==> \n", df1 - s1, sep="")
df2 = pd.DataFrame(np.arange(1,13).reshape(4,3), index=list('bcde'), columns=list('CDE'))
print ("df1 * df2 ==> \n", df1 * df2, sep='')

print ("df1.div(df2, fill_value=0) ==>\n", df1.div(df2, fill_value=0), sep='')


#pd.DataFrame.apply(func, axis=0)

print (np.random.rand(6,4))
print (np.random.randn(6,4))
df0 = pd.DataFrame(np.random.rand(6,4), index = pd.date_range('2016-01-06', periods=6), columns=list('ABCD'))
print (df0)

print (df0.apply(max, axis=0))

f = lambda x:x.max()-x.min()
print (df0.apply(f, axis=1))

# 缺失值处理
df3 = df1.mul(df2, fill_value=0)
print (df3)
print (df3.isnull())
print (df3.notnull())

print (df3.A[df3.A.notnull()])














