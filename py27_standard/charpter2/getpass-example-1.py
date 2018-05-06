# -*- coding:utf-8 -*-
# Example 2-25. 使用 getpass 模块  
# File: getpass-example-1.py 
 
import getpass 
 
usr = getpass.getuser() 
 
pwd = getpass.getpass("enter password for user %s: " % usr) 
 
print usr, pwd




