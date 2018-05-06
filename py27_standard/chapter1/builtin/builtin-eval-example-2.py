# -*- coding:utf-8 -*-
# Example 1-18. 使用 eval 函数执行任意命令

print eval("__import__('os').getcwd()") 
print eval("__import__('os').remove('file')")