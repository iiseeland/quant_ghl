# -*- coding:utf-8 -*-
# Example 6-1. 使用 rfc822 模块  
# File: rfc822-example-1.py 
 
import rfc822 
 
file = open("samples/sample.eml") 
 
message = rfc822.Message(file) 
 
for k, v in message.items(): 
    print k, "=", v 
 
print len(file.read()), "bytes in body" 




