# -*- coding:utf-8 -*-
# 


import md5 
import string 
import base64 


def is_right_result(hex):
    return '0' == hex[0] and '0'==hex[1] and '0' == hex[2] and '0' == hex[3] and '0' == hex[4] and '0' == hex[5]

    
def hash_func(src):
    hash = md5.new()
    hash.update(src)
    return hash.hexdigest()
    
src = 'spam, spam, and eggs'

i = 0
while 1:
    if is_right_result(hash_func(src+repr(i))):
        break
    i = i+1
    

print i, 
print hash_func(src + repr(i))    