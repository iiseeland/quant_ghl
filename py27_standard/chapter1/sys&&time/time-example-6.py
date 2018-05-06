# -*- coding:utf-8 -*-
# Example 1-81. 使用 time.strptime 函数解析时间  
# File: time-example-6.py 
 
import time 
 
# make sure we have a strptime function! 
# 确认有函数 strptime 
try: 
    strptime = time.strptime 
except AttributeError: 
    from strptime import strptime 
 
print strptime("31 Nov 00", "%d %b %y") 
print strptime("1 Jan 70 1:30pm", "%d %b %y %I:%M%p") 




