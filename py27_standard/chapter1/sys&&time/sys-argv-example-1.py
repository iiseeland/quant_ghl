# -*- coding:utf-8 -*-
# Example 1-66. 使用 sys 模块获得脚本的参数

import sys 
 
print "script name is", sys.argv[0] 
 
if len(sys.argv) > 1: 
    print "there are", len(sys.argv)-1, "arguments:" 
    for arg in sys.argv[1:]: 
        print arg 
else: 
    print "there are no arguments!"


