# -*- coding:utf-8 -*-
# Example 2-9. 使用 StringIO 模块向内存文件写入内容  
# File: stringio-example-2.py 
 
import StringIO 
 
file = StringIO.StringIO() 
file.write("This man is no ordinary man. ") 
file.write("This is Mr. F. G. Superman.") 
 
print file.getvalue()




