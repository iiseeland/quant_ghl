# -*- coding:utf-8 -*-
# Example 1-29. 使用 os 模块改变当前工作目录 

import os 
 
# where are we? 
cwd = os.getcwd() 
print "1", cwd 
 
# go down 
os.chdir("samples") 
print "2", os.getcwd() 
 
# go back up 
os.chdir(os.pardir) 
print "3", os.getcwd()


