# -*- coding:utf-8 -*-
# Example 4-3. 使用阵列将字符串转换为整数列表  
# File: array-example-3.py 
 
import array 
 
a = array.array("i", "fish license") # signed integer 
 
print a 
print repr(a.tostring()) 
print a.tolist()




