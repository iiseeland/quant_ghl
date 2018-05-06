# -*- coding:utf-8 -*-
# Example 4-7. 使用 xdrlib 模块  
# File: xdrlib-example-1.py 
 
import xdrlib 
 # 
# create a packer and add some data to it 
 
p = xdrlib.Packer() 
p.pack_uint(1) 
p.pack_string("spamq") 
 
data = p.get_buffer() 
 
print "packed:", repr(data) 
 
# 
# create an unpacker and use it to decode the data 
 
u = xdrlib.Unpacker(data) 
 
print "unpacked:", u.unpack_uint(), repr(u.unpack_string()) 
 
u.done()




