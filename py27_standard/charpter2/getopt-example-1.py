# -*- coding:utf-8 -*-
# Example 2-23. 使用 getopt 模块  
# File: getopt-example-1.py 
 
import getopt 
import sys 
 
# simulate command-line invocation 
# 模仿命令行参数 
sys.argv = ["myscript.py", "-l", "-d", "directory", "filename", 'filename2'] 
 
# process options 
# 处理选项 
# 选项名后的冒号(:) 意味这这个选项必须有额外的参数
opts, args = getopt.getopt(sys.argv[1:], "ld:") 
 
long = 0 
directory = None  

for o, v in opts: 
    if o == "-l": 
        long = 1 
    elif o == "-d": 
        directory = v 
 
print "long", "=", long 
print "directory", "=", directory 

print "arguments", "=", args




