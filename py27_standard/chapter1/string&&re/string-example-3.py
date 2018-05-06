# -*- coding:utf-8 -*-
# Example 1-53. 使用 string 模块将字符串转为数字

import string 
 
print int("4711"), 
print string.atoi("4711"), 
print string.atoi("11147", 8), # octal 八进制 
print string.atoi("1267", 16), # hexadecimal 十六进制 
print string.atoi("3mv", 36) # whatever... 
 
print string.atoi("4711", 0), 
print string.atoi("04711", 0), 
print string.atoi("0x4711", 0) 
 
print float("4711"), 
print string.atof("1"), 
print string.atof("1.23e5")


