# -*- coding:utf-8 -*-
# Example 4-19. 使用 base64 模块编码字符串  
# File: base64-example-2.py 
 
import base64 
 
MESSAGE = "life of brian11" 
 
data = base64.encodestring(MESSAGE) 
 
original_data = base64.decodestring(data) 
 
print "original:", repr(MESSAGE) 
print "encoded data:", repr(data) 
print "decoded data:", repr(original_data)




