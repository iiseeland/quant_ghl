# -*- coding:utf-8 -*-
# Example 2-4. 使用 shutil 复制文件  
# File: shutil-example-1.py 
 
import shutil 
import os 
 
for file in os.listdir("."): 
    if os.path.splitext(file)[1] == ".py": 
        print file 
        shutil.copy(file, os.path.join("backup", file))




