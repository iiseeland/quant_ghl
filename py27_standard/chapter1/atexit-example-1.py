# -*- coding:utf-8 -*-
# Example 1-78. 使用 atexit 模块  
# File: atexit-example-1.py 
 
import atexit 
 
def exit(*args): 
    print "exit", args 
 
# register two exit handler 
atexit.register(exit) 
atexit.register(exit, 1) 
atexit.register(exit, "hello", "world") 




