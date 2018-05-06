# -*- coding:utf-8 -*-
# Example 1-64. 使用 copy/deepcopy 模块复制对象

import copy 
 
a = [[1],[2],[3]] 
b = copy.copy(a) 
#b = copy.deepcopy(a)
 
print "before", "=>" 
print a 
print b 
 
# modify original 
a[0][0] = 0 
a[1] = None 
 
print "after", "=>" 
print a 
print b


