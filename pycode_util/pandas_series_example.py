# -*- coding: utf-8 -*-
'''
Created on 2018年5月5日

@author: isld
'''
import pandas as pd
import numpy as np
from _datetime import datetime

s1 = pd.Series()
print (type(s1))
s2 = pd.Series(data = [1,3,5,7,9], index=['a', 'b', 'c', 'd', 'e'])
#s2.index = ['a', 'b', 'c', 'd', 'e']
print (s2)
s2['f'] = 11
print  ("s2[['b', 'c', 'd']] =>\n", s2[['b', 'c', 'd']])
s3 = pd.Series({'a':1, 'b':3, 'c':5, 'd':7})
print (s3)

print ("pd.Series(np.random.randn(5)) =>\n", pd.Series(np.random.randn(5)))
print ("pd.Series(np.arange(2,6)) => \n", pd.Series(np.arange(2,6)))


s = pd.Series(np.arange(1,101))
print ("s.head(4) =>\n", s.head(4))
print ("s.tail(5) => \n", s.tail(5))
print ("s.take([4,8,2]) =>\n", s.take([4,8,2]))
print ("s[[4,8,2]] =>", s[[4,8,2]])

# Series 切片：标签切片，包括起始标签和结束标签，位置切片包括起始位置和结束位置
s = pd.Series({'c':1, 'a': 2, 'd':3, 'b':4, 'e':5, 'f':6})
print ("s =>\n", s)
print ("s['a':'b'] =>\n", s['a':'b'])
print ("s[1:3]=>\n", s[1:3])


d = datetime(2016, 1, 1)
print (type(d), d)

d = pd.Timestamp(d)
print (type(d), d)

ser = pd.Series(1, index=[d])
print (ser)

dates = ['2016-01-06', '2016-01-07', '2016-01-08', '2016-02-01', '2016-03-02']
data = np.arange(5)
ser = pd.Series(data, index = pd.to_datetime(dates))
print (ser.index)
print ('datetime series =>\n', ser)
print ("ser['2016'] =>", ser['2016'])
print ("ser['2016-01'] =>", ser['2016-01'])
print ("ser['2016-01':'2016-02'] =>", ser['2016-01':'2016-02'])
print ("ser['2016-01-5':'2016-02-01'] =>", ser['2016-01-5':'2016-02-01'])

# 数据滞后，数据超前
print ('ser.shift(1) => \n', ser.shift(1))
print ('ser.shift(-1) => \n', ser.shift(-1))

data = [20.34, 20.56, 21.01, 20.65, 21.34]
dates = ['2016-01-06', '2016-01-07', '2016-01-08', '2016-01-09', '2016-01-10']
ser = pd.Series(data, pd.to_datetime(dates))
print ((ser-ser.shift(1))/ser.shift(1))
print ("ser index type.", type(ser.index))

