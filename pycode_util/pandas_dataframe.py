# -*- coding: utf-8 -*-
'''
Created on 2018年5月6日

@author: isld
'''
'''
简单地说： DataFrame是共享同一个Index的Series集合
'''

import pandas as pd
import numpy as np
#import MySQLdb

pydates = ['2016-01-06', '2016-01-07', '2016-01-08', '2016-01-09', '2016-01-10', '2016-01-11' ]
pddates = pd.to_datetime(pydates)

df = pd.DataFrame(np.array(np.arange(-8,16)).reshape(6,4), index = pddates, columns=list("ABCD"))
print(df)

'''
pd.read_table("date_file", sep='\t', header=None, names=None)
pd.read_csv('data_file', sep=',', header=None)

mysql_cn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='pwd123',db='stock')
dfn=pd.read_sql('select * from company limit 10;', con=mysql_cn)
mysql_cn.close()
'''

print ("df.head(3) =>\n", df.head(3), sep='')
print ("df.tail(2) =>\n", df.tail(2), sep='')

print ("df.columns =>\n", df.columns, sep='')
print ("df.index =>\n", df.index, sep='')
print ("df.values =>\n", df.values, sep='')

print ("df.describe() =>\n", df.describe(), sep='')

# 索引和切片
print ("df[1:3]  ==>\n", df[1:3], sep='')
print ("df['A'] ==>\n", df['A'], sep ='')
print ("df[['A', 'C']] ==> \n", df[['A', 'C']], sep = '')
print ("df[df['A']>0] ==>\n", df[df['A']>0], sep = '')

# 标签索引与切片
print ("df.loc[:, 'A'] ==> \n", df.loc[:, 'A'], sep = '')
print ("df.loc[:, 'A':'C'] ==> \n", df.loc[:, 'A':'C'], sep = '')
print ("df.loc[pddates[0:2], 'A':'C'] ==>\n", df.loc[pddates[0:2], 'A':'C'], sep = '')
print ("df.loc[pddates[0], 'A'] ==> \n", df.loc[pddates[0], 'A'], sep = '')
print ("df.at[pddates[0], 'A'] ==> \n", df.at[pddates[0], 'A'], sep = '')
print ("df.loc[df.loc[:,'A']>0] ==> \n", df.loc[df.loc[:,'A']>0], sep = '')

#位置索引与切片
# 提取某行
print ("df.iloc[2] ==>\n", df.iloc[2], sep = '')
# 提取某列
print ("df.iloc[:,2] ==> \n", df.iloc[:,2], sep = '')
# 提取某几行某几列
print ("df.iloc[[1,4], [2,3]] ==>\n", df.iloc[[1,4], [2,3]], sep = '')
# 切片
print ("df.iloc[1:4, 2:4] ==>\n", df.iloc[1:4, 2:4], sep = '')

# 提取特定标量
print ("df.iloc[3,3] ==> \n", df.iloc[3,3], sep = '')
print ("df.iat[3,3] ==> \n", df.iat[3,3], sep = '')
# 根据boolean值提取
print ("df.loc[:, df.iloc[3]>0] ==> \n", df.loc[:, df.iloc[3]>0], sep = '')


# 广义索引与切片
print (" \n\n广义索引与切片")
# 双行切片
print ("df.ix[2:5] ==> \n", df.ix[2:5], sep = '')
# 获取某几行，某几列
print ("df.ix[[1,3],2] ==>\n", df.ix[[1,3],2], sep = '')
print ("df.ix[[1,3], 'C'] ==> \n", df.ix[[1,3], 'C'],  sep = '')
# 对行与列进行切片
print ("df.ix[1:3, 'A':'C'] ==>\n", df.ix[1:3, 'A':'C'], sep = '')

# 根据boolean值进行提取
print ("df.ix[1:3, df.iloc[3]>0] ==> \n", df.ix[1:3, df.iloc[3]>0], sep = '')


# 转置
print ("df.T ==> \n", df.T, sep = '')




















