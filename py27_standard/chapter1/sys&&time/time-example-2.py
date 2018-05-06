﻿# -*- coding:utf-8 -*-
# Example 1-80. 使用 time 模块格式化时间输出  
# File: time-example-2.py 
 
import time 
 
now = time.localtime(time.time()) 
utc = time.time()
 
print "now: ", now,
print "utc: ", utc, 
 
print time.asctime(now) 
print time.strftime("%y/%m/%d %H:%M", now) 
print time.strftime("%a %b %d", now) 
print time.strftime("%c", now) 
print time.strftime("%I %p", now) 
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now) 
 
# do it by hand... 
year, month, day, hour, minute, second, weekday, yearday, daylight = now 
print "%04d-%02d-%02d" % (year, month, day) 
print "%02d:%02d:%02d" % (hour, minute, second) 
print ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday



