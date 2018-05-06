# -*- coding:utf-8 -*-
# Example 2-5. 使用 shutil 模块复制/删除目录树  
# File: shutil-example-2.py 
 
import shutil 
import os 
 
SOURCE = "samples" 
BACKUP = "samples-bak" 
 
# create a backup directory 
shutil.copytree(SOURCE, BACKUP) 
 
print os.listdir(BACKUP) 
 
# remove it 
shutil.rmtree(BACKUP) 
 
print os.listdir(BACKUP)




