# -*- coding: utf-8 -*-
'''
Created on 2018年5月5日

@author: isld
'''
s1=set([20,30,40,50,'python'])
s3={20,30,40,30,50,60,'python'}
print (s3)
l = [30,20,30,40,50,'python']
s2 = set(l)
print (s2)

s1.add('finace')
s1.remove('finace')

# 对称差
s4={1,2,3,4,5}
s5 = {4,5,6,7,8}
print (s4 ^ s5)

fs = frozenset(l)


'''
s1 | s2 set.union()
s1 & s2 set.intersection()
s1 - s2 set.difference()
s1 ^ s2 set.symmetric_difference()
set.isdisjoint()
s1 <= s2 set.issubset()
s1 >= s2 set.issuperset()
'''