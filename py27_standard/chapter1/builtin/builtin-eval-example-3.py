# -*- coding:utf-8 -*-
# Example 1-19. 安全地使用 eval 函数求值

print eval("__import__('os').getcwd()", {}) 
print eval("__import__('os').remove('file')", {"__builtins__": {}})