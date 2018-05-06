# -*- coding:utf-8 -*-
# Example 1-28. 使用 os 列出目录下的文件

import os 
 
for file in os.listdir("samples"): 
    print file 