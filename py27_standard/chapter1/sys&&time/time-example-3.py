# -*- coding:utf-8 -*-
# Example 1-83. 使用 time 模块将本地时间元组转换为时间值(整数)  
# File: time-example-3.py 
 
import time 
 
t0 = time.time() 
tm = time.localtime(t0) 
 
print tm 
 
print t0 
print time.mktime(tm)




