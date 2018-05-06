# -*- coding:utf-8 -*-
# Example 2-20. 使用 traceback Module 模块编码 Traceback 对象  
# File: traceback-example-3.py 
 
import traceback 
import sys 
 
def function(): 
    raise IOError, "an i/o error occurred" 
 
try:     function() 
except: 
    info = sys.exc_info() 
    for file, lineno, function, text in traceback.extract_tb(info[2]): 
        print file, "line", lineno, "in", function 
        print "=>", repr(text) 
    print "** %s: %s" % info[:2]




