# -*- coding:utf-8 -*-
# Example 2-18. 使用 traceback 模块打印跟踪返回信息  
# File: traceback-example-1.py 
 
# note! importing the traceback module messes up the 
# exception state, so you better do that here and not 
# in the exception handler 
# 注意! 导入 traceback 会清理掉异常状态, 所以 
# 最好别在异常处理代码中导入该模块 
import traceback 
try: 
    raise SyntaxError, "example" 
except: 
    traceback.print_exc()

print "hello."



