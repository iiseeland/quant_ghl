# -*- coding:utf-8 -*-
# Example 2-26. 使用 glob 模块  
# File: glob-example-1.py 
 
import glob 

# glob 根据给定模式生成满足该模式的文件名列表 
for file in glob.glob("samples/*.jpg"): 
    print file




