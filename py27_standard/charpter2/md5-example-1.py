# -*- coding:utf-8 -*-
# Example 2-35. 使用 md5 模块  
# File: md5-example-1.py 
 
import md5 
 
hash = md5.new() 
hash.update("spam, spam, and eggs")  
print repr(hash.digest())




