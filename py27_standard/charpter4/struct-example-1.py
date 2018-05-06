# -*- coding:utf-8 -*-
# Example 4-6. 使用 struct 模块  
# File: struct-example-1.py 
 
import struct 

# "ihb"是格式化字符串，代表后边的类型 
# native byteorder 
buffer = struct.pack("ihb", 1, 2, 3) 
print repr(buffer) 
print struct.unpack("ihb", buffer) 
 
# data from a sequence, network byteorder 
data = [1, 2, 3] 
buffer = apply(struct.pack, ("!ihb",) + tuple(data)) 
print repr(buffer) 
print struct.unpack("!ihb", buffer) 
 
# in 2.0, the apply statement can also be written as: 
# buffer = struct.pack("!ihb", *data)




