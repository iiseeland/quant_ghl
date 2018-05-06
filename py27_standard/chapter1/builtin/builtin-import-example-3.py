# -*- coding:utf-8 -*-
# Example 1-7. 使用 _ _import_ _ 函数实现 延迟导入

class LazyImport: 
    def __init__(self, module_name): 
        self.module_name = module_name
        self.module = None 
    def __getattr__(self, name): 
        if self.module is None: 
            self.module = __import__(self.module_name) 
        return getattr(self.module, name) 
 
string = LazyImport("string") 
 
print string.lowercase