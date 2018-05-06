# -*- coding:utf-8 -*-
# Example 2-27. 使用 fnmatch 模块匹配文件  
# File: fnmatch-example-1.py 
 
import fnmatch 
import os 
 
for file in os.listdir("samples"): 
    if fnmatch.fnmatch(file, "*.jpg"): 
        print file




