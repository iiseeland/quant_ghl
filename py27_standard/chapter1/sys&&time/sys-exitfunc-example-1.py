# -*- coding:utf-8 -*-
# Example 1-77. 另一种捕获 sys.exit 调用的方法
# 程序正常退出，也会触发到函数调用

import sys 
 
def exitfunc(): 
    print "world" 
 
sys.exitfunc = exitfunc 
 
print "hello" 
sys.exit(1) 
print "there" # never printed # 不会被 print


