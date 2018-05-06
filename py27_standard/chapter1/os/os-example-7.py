# -*- coding:utf-8 -*-
# Example 1-31. 使用 os 模块创建/删除目录

import os 
 
os.mkdir("test") 
os.rmdir("test") 

# 如果需要删除非空目录, 你可以使用 shutil 模块中的 rmtree 函数 
os.rmdir("samples1") # this will fail


