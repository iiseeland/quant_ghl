# -*- coding:utf-8 -*-
# Example 1-37. 使用 os 模块调用其他程序 (Windows)

import os 
import string 
 
# for use spawn, use should find executable yourself, and while exec spawn, a new process is started
 
def run(program, *args): 
    # find executable 
    for path in string.split(os.environ["PATH"], os.pathsep): 
        file = os.path.join(path, program) + ".exe" 
        try: 
            return os.spawnv(os.P_WAIT, file, (file,) + args) 
        except os.error: 
            pass 
    raise os.error, "cannot find executable" 
 
run("python", "hello.py") 
 
print "goodbye"


