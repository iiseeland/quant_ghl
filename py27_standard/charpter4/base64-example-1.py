# -*- coding:utf-8 -*-
# Example 4-18. 使用 base64 模块编码文件  
# File: base64-example-1.py 
 
import base64 
 
MESSAGE = "life of brian" 
 
file = open("out.txt", "w") 
file.write(MESSAGE) 
file.close() 
 
base64.encode(open("out.txt"), open("out.b64", "w")) 
base64.decode(open("out.b64"), open("out.txt", "w")) 
 
print "original:", repr(MESSAGE) 
print "encoded message:", repr(open("out.b64").read()) 
print "decoded message:", repr(open("out.txt").read()) 
 


