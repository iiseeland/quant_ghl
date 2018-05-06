# -*- coding: utf-8 -*-
'''
Created on 2018年5月5日

@author: isld
'''
import numpy as np

arry1=np.array(range(6))
print (arry1)
print(arry1.shape)
arry1.shape=2,3
print(arry1)

arry2 = arry1.reshape(3,2)
print ("arry2 ==> ", arry2)
print("arry2[1] ==>", arry2[1])


a = np.zeros((3,5))
a = np.ones((2,3,4))
a= np.empty((3,2))
print (a)

a= np.array(range(1,26,6))
print ("range(1,26,6) =>", a)
a = np.linspace(1,26,6)
print ("linspace(1,26,6) =>", a)
print (a[[0,1,4]])

# 创建一维数组
ar1 = np.array(np.arange(5))
print (ar1)

# 数组中每个元素都加4
np.add(ar1, 4)

# 创建一维数组ar2
ar2 = np.array([2,3,4,5,6])

print (ar1+ar2)
print (np.add(ar1, ar2))

a = np.array([10,20,30,50,60])
print (type(a))
b = np.arange(5)
print (type(b))
print ("a-b =>", a-b)
print ("b ** 2 => ", b**2)
print ("10 * np.cos(a) =>", 10 * np.cos(a))
print ("a < 40 =>", a < 40)


'''
np.add(a, b, [c])            =>        c = a+b
np.substrack(a, b, [c])      =>        c = a-b
np.multipl(a, b, [c])        =>        c = a*b
np.divide(a, b, [c])         =>        c = a/b
np.mod(a, b, [c])            =>        c = a%b
no.power(a, b, [c])          =>        c = a**b
np.square(a, [c])            =>        开平方
'''











