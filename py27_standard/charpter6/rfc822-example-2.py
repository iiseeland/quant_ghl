# -*- coding:utf-8 -*-
# Example 6-2. 使用 rfc822 模块解析标头字段  
# File: rfc822-example-2.py 
 
import rfc822 
 
file = open("samples/sample.eml") 
 
message = rfc822.Message(file) 
print message.getdate("date") 
print message.getaddr("from") 
print message.getaddrlist("to")




