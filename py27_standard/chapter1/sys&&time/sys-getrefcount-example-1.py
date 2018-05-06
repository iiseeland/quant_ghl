# -*- coding:utf-8 -*-
# Example 1-70. 使用 sys 模块获得引用记数

import sys 
 
variable = 1234 
 
print sys.getrefcount(0) 
print sys.getrefcount(variable) 
print sys.getrefcount(None)


