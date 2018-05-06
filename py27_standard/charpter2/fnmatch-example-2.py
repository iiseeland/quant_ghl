# -*- coding:utf-8 -*-
# Example 2-28. 使用 fnmatch 模块将模式转换为正则表达式  
# File: fnmatch-example-2.py 
 
import fnmatch 
import os, re 
 
pattern = fnmatch.translate("*.jpg") 
 
for file in os.listdir("samples"): 
    if re.match(pattern, file): 
        print file 
 
print "(pattern was %s)" % pattern




