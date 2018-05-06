# -*- coding:utf-8 -*-
# Example 4-9. 使用 marshal 模块组合不连续数据  
# File: marshal-example-1.py 
 
import marshal 
 
value = ( 
    "this is a string", 
    [1, 2, 3, 4], 
    ("more tuples", 1.0, 2.3, 4.5), 
    "this is yet another string" 
    ) 
 
data = marshal.dumps(value)  
# intermediate format 
print type(data), len(data) 
 
print "-*"*25 
print repr(data) 
print "-*"*25 
 
print marshal.loads(data)




