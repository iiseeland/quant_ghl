# -*- coding:utf-8 -*-
# Example 4-20. 使用 base64 模块做基本验证  
# File: base64-example-3.py 
 
import base64 
 
def getbasic(user, password): 
    # basic authentication (according to HTTP) 
    return base64.encodestring(user + ":" + password) 
 
print getbasic("Aladdin", "open sesame")




