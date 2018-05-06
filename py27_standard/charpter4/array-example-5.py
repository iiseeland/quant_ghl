# -*- coding:utf-8 -*-
# Example 4-5. 使用 sys.byteorder 属性判断平台字节序( Python 2.0 及以后)  
# File: sys-byteorder-example-1.py 
 
import sys 
 
# 2.0 and later 
if sys.byteorder == "little": 
    print "little-endian platform (intel, alpha)" 
else: 
    print "big-endian platform (motorola, sparc)"




