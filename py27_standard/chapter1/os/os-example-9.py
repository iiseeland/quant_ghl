# -*- coding:utf-8 -*-
# Example 1-41. 使用 os 模块终止当前进程

import os 
import sys 
 
try: 
#    sys.exit(1)
    pass
except SystemExit, value: 
    print "caught exit(%s)" % value 
 
try: 
    os._exit(2) 
except SystemExit, value: 
    print "caught exit(%s)" % value 
 
print "bye!"


