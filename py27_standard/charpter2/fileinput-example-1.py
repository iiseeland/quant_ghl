# -*- coding:utf-8 -*-
# Example 2-1. 使用 fileinput 模块循环一个文本文件  
# File: fileinput-example-1.py 
 
import fileinput 
import sys 
 
for line in fileinput.input("samples/sample.txt"): 
    sys.stdout.write("-> ") 
    sys.stdout.write(line)




