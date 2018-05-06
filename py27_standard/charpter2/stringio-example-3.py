# -*- coding:utf-8 -*-
# Example 2-10. 使用 StringIO 模块捕获输出  
# File: stringio-example-3.py 
 
import StringIO 
import string, sys 
 
stdout = sys.stdout 
 
sys.stdout = file = StringIO.StringIO() 
 
print """ 
According to Gbaya folktales, trickery and guile 
are the best ways to defeat the python, king of 
snakes, which was hatched from a dragon at the 
world's start. -- National Geographic, May 1997 
""" 
 
sys.stdout = stdout 
 
print string.upper(file.getvalue())




