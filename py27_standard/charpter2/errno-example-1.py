# -*- coding:utf-8 -*-
# Example 2-21. 使用 errno 模块  
# File: errno-example-1.py 
 
import errno 
 
try: 
    fp = open("no.such.file") 
except IOError, (error, message): 
    if error == errno.ENOENT: 
        print "no such file" 
    elif error == errno.EPERM: 
        print "permission denied" 
    else: 
        print message




