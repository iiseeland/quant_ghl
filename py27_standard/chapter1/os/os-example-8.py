# -*- coding:utf-8 -*-
# Example 1-34. 使用 os 执行操作系统命令

import os 
 
if os.name == "nt": 
    command = "dir"  
else: 
    command = "ls -l" 

# 执行系统命令    
os.system(command)


