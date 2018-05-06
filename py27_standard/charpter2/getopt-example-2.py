# -*- coding:utf-8 -*-
# Example 2-24. 使用 getopt 模块处理长选项  
# File: getopt-example-2.py 
 
import getopt 
import sys 
 
# simulate command-line invocation 
# 模仿命令行参数 
sys.argv = ["myscript.py", "--echo", "--printer", "lp01", "message"] 
 
# 如果一个选项名称以等号(=) 结尾, 那么它必须有一个附加参数 
opts, args = getopt.getopt(sys.argv[1:], "ep:", ["echo", "printer="]) 
 
# process options 
# 处理选项 
echo = 0 
printer = None 
 
for o, v in opts: 
    if o in ("-e", "--echo"): 
        echo = 1
        print "echo v: ", repr(v)
    elif o in ("-p", "--printer"): 
        printer = v 
 
print "echo", "=", echo 
print "printer", "=", printer 
print "arguments", "=", args




