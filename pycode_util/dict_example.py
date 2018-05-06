# -*- coding: utf-8 -*-
'''
Created on 2018年5月5日

@author: isld
'''


s1 = {'Date':'02-Mar-2015', 'Open':3332.7,'High':3336.8,'Low':3298.7, 'Close':3336.3}
s2 = dict({'Date':'02-Mar-2015', 'Open':3332.7,'High':3336.8,'Low':3298.7, 'Close':3336.3})
s3 = dict(Date='02-Mar-2015', Open=3332.7,High=3336.8,Low=3298.7, Close=3336.3)
s4 = dict([('Date', '02-Mar-2015'),('Open', 3332.7),('High', 3336.8),('Low', 3298.7),('Close', 3336.3)])
s5 = dict(zip(['Date', 'Open', 'High', 'Low', 'Close'], ['02-Mar-2015', 3332.7, 3336.8, 3298.7, 3336.3]))
print (s1==s2==s3==s4==s5)
print ("items ==>", s1.items())
print ("keys ==>", s1.keys())
print ("values ==>", s1.values())

s1["index"]='00001.ss'
print ('s1 add index==>', s1)
del s1['index']
print ('s1 del index==>', s1)

scopy = s1.copy()
scopy.clear()
print ("s1 after copy clear ==>", s1)
