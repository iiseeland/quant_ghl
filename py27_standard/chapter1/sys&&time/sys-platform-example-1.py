# -*- coding:utf-8 -*-
# Example 1-71. 使用 sys 模块获得当前平台

import sys 
 
# 
# emulate "import os.path" (sort of)... 
 
if sys.platform == "win32": 
    import ntpath 
    pathmodule = ntpath 
elif sys.platform == "mac": 
    import macpath 
    pathmodule = macpath 
else: 
    # assume it's a posix platform 
    import posixpath 
    pathmodule = posixpath 
 
print pathmodule


