# -*- coding:utf-8 -*-
# Example 1-23. 使用 execfile 函数

execfile("hello.py") 
print 
def EXECFILE(filename, locals=None, globals=None): 
    exec compile(open(filename).read(), filename, "exec") in locals, globals 
 
EXECFILE("hello.py")


