# -*- coding:utf-8 -*-
# Example 4-14. 使用 copy_reg 模块实现 code 对象的 pickle 操作  
# File: copy-reg-example-2.py 
 
import copy_reg 
import pickle, marshal, types 
 
# 
# register a pickle handler for code objects 
 
def code_unpickler(data): 
    return marshal.loads(data) 
 
def code_pickler(code): 
    return code_unpickler, (marshal.dumps(code),) 
 
copy_reg.pickle(types.CodeType, code_pickler, code_unpickler) 
 
# 
# try it out 
 
CODE = """ 
print "suppose he's got a pointed stick" 
""" 
 
code = compile(CODE, "<string>", "exec") 
 
exec code 
exec pickle.loads(pickle.dumps(code))




