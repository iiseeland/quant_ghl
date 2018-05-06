# -*- coding:utf-8 -*-
# Example 2-6. 使用 tempfile 模块创建临时文件  
# File: tempfile-example-1.py 
 
import tempfile 
import os 
 
tempfile = tempfile.mktemp() 
 
print "tempfile", "=>", tempfile 
 
file = open(tempfile, "w+b") 
file.write("*" * 1000) 
file.seek(0) 
print len(file.read()), "bytes" 
file.close() 
 
try: 
    # must remove file when done 
    os.remove(tempfile) 
except OSError: 
    pass 
 




