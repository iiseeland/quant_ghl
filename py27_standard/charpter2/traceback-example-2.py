# -*- coding:utf-8 -*-
# Example 2-19. 使用 traceback 模块将跟踪返回信息复制到字符串  
# File: traceback-example-2.py 
 
import traceback 
import StringIO 
 
try: 
    raise IOError, "an i/o error occurred" 
except: 
    fp = StringIO.StringIO() 
    traceback.print_exc(file=fp) 
    message = fp.getvalue() 
 
    print "failure! the error was:", repr(message)




