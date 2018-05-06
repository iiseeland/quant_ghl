# -*- coding:utf-8 -*-
# Example 2-7. 使用 tempfile 模块打开临时文件  
# File: tempfile-example-2.py 
 
import tempfile 
 
file = tempfile.TemporaryFile() 
for i in range(100): 
    file.write("*" * 100) 
 
file.close() # removes the file!




