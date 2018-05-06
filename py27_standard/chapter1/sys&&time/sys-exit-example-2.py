# -*- coding:utf-8 -*-
# Example 1-76. 捕获 sys.exit调用

import sys 
 
print "hello" 
 
try: 
    sys.exit(1) 
except SystemExit: 
    pass 
 
print "there" 


