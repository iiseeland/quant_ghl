# -*- coding:utf-8 -*-
# Example 1-6. 使用 _ _import_ _ 函数获得特定函数

def getfunctionbyname(module_name, function_name): 
    module = __import__(module_name) 
    return getattr(module, function_name) 
 
print repr(getfunctionbyname("dumbdbm", "open"))
