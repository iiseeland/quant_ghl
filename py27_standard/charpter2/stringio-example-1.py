# -*- coding:utf-8 -*-
# Example 2-8. 使用 StringIO 模块从内存文件读入内容  
# File: stringio-example-1.py 
 
import StringIO 
 
MESSAGE = "That man is depriving a village somewhere of a computer scientist." 
 
file = StringIO.StringIO(MESSAGE) 
 
print file.read()




