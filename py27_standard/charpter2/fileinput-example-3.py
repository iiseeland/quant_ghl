# -*- coding:utf-8 -*-
# Example 2-3. 使用 fileinput 模块将 CRLF 改为 LF  
# File: fileinput-example-3.py 
 
import fileinput, sys 
 
for line in fileinput.input(inplace=1): 
    # convert Windows/DOS text files to Unix files 
    if line[-2:] == "\r\n": 
        line = line[:-2] + "\n" 
    sys.stdout.write(line)




