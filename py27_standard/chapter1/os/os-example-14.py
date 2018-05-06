# -*- coding:utf-8 -*-
# Example 1-40. 使用 os 模块使脚本作为守护执行 (Unix)

import os 
import time 
 
pid = os.fork()  
if pid: 
    os._exit(0) 
    # kill original print "daemon started" 
time.sleep(10) 
print "daemon terminated"


