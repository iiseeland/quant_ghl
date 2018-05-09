# -*- coding: utf-8 -*-
'''
Created on 2018

@author: isld
'''
import pandas as pd
import numpy as np
#import MySQLdb

pydates = ['2016-01-06', '2016-01-07', '2016-01-08', '2016-01-09', '2016-01-10', '2016-01-11' ]
pddates = pd.to_datetime(pydates)

df = pd.DataFrame(np.random.randn(6,4), index = pddates, columns=list("ABCD"))
print(df)

print (df.sort_values(by='A', ascending=False))
dfrank = df.rank();
print ("df.rank() => \n", dfrank, sep = '')
print ("df.rank(acsending=False) => \n", df.rank(ascending=False), sep = '')

ser = pd.Series([1,2,3,4,5,6], index=pd.date_range('2016-01-07',  periods = 6))
df["E"] = ser
print ("add column e: ==>\n", df, sep = '')

# 合并操作 横向
df = df[list('ABCD')]
print ("pd.concat([df, ser], axis=1) ==>\n", pd.concat([df, ser], axis=1), sep = '')


# 合并操作 纵向
df1 = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}, index = pd.date_range("2016-01-07", periods=3))
print (df1)
print (df.append(df1))

print ("pd.concat([df, df1], join='inner') ==>\n", pd.concat([df, df1], join='inner'), sep = '')

print ("df.drop(pddates[1:3]) ==>\n", df.drop(pddates[1:3]), sep = '')
print ("df.drop('A') ==>\n", df.drop('A', axis=1), sep = '')


del df['A']
print ("after del ==> \n", df, sep = '')

df.loc[pydates[2], "C"] = 2

# 替换整列
df.loc[:, "B"] = np.arange(0, len(df))

newidx = pd.date_range('2016-01-08', periods=7)
print (df.reindex(newidx, columns=list('ABCD')))














