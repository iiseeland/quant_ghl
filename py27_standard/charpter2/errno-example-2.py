# -*- coding:utf-8 -*-
# Example 2-22. 使用 errorcode 字典  
# File: errno-example-2.py 
 
import errno 
 
try: 
    fp = open("no.such.file") 
except IOError, (error, message): 
    print error, repr(message) 
    print errno.errorcode[error]




