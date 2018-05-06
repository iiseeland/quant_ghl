# -*- coding:utf-8 -*-
# Example 1-35. 使用 os 模块启动新进程

import os 
import sys 
 
program = "python" 
arguments = ["hello.py"] 
 
print os.execvp(program, (program,) +  tuple(arguments)) 
print "goodbye" # this will never be excuted.


