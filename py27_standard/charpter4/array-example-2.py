# -*- coding:utf-8 -*-
# Example 4-2. 作为普通序列操作阵列  
# File: array-example-2.py 
 
import array 
 
a = array.array("B", [1, 2, 3]) 
 
a.append(4) 
 
a = a + a 
 
a = a[2:-2] 
 
print a 
print repr(a.tostring()) 
for i in a: 
    print i,




