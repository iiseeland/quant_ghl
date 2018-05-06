# -*- coding:utf-8 -*-
# Example 4-10. 使用 marshal 模块处理代码  
# File: marshal-example-2.py 
 
import marshal 
 
script = """ 
print 'hello' 
""" 
 
code = compile(script, "<script>", "exec") 
 
data = marshal.dumps(code) 
 
# intermediate format 
print type(data), len(data) 
 
print "-"*50 
print repr(data) 
print "-"*50 
exec marshal.loads(data)




