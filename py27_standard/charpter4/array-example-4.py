# -*- coding:utf-8 -*-
# Example 4-4. 使用 array 模块判断平台字节序  
# File: array-example-4.py 
 
import array 
 
def little_endian(): 
    return ord(array.array("i",[1]).tostring()[0]) 
 
if little_endian(): 
    print "little-endian platform (intel, alpha)" 
else: 
    print "big-endian platform (motorola, sparc)"




