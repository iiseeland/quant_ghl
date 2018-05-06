# -*- coding:utf-8 -*-
# Example 2-11. 使用 cStringIO 模块  
# File: cstringio-example-1.py 
 
import cStringIO 
 
MESSAGE = "That man is depriving a village somewhere of a computer scientist." 
 
file = cStringIO.StringIO(MESSAGE)  
print file.read()




