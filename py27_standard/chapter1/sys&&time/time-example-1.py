# -*- coding:utf-8 -*-
# Example 1-79. 使用 time 模块获取当前时间  
# File: time-example-1.py 
 
import time 
 
now = time.time() 
 
print now, "seconds since", time.gmtime(0)[:6] 
print 
print "or in other words:" 
print "- local time:", time.localtime(now) 
print "- utc:", time.gmtime(now)




