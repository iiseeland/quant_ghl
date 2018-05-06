# -*- coding:utf-8 -*-

# Example 1-9. 使用 dir 函数
# dir 返回由给定模块, 类, 实例, 或其他类型的所有成员组成的列表

def dump(value): 
    print value, "=>", dir(value), "\r\n" 
 
import sys 
 
dump(0) 
dump(1.0) 
dump(0.0j) # complex number 
dump([]) # list 
dump({}) # dictionary 
dump("string") 
dump(len) # function 
dump(sys) # module 