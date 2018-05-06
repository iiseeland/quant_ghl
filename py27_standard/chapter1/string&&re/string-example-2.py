# -*- coding:utf-8 -*-
# Example 1-52. 使用字符串方法替代 string 模块函数

text = "Monty Python's Flying Circus" 
 
print "upper", "=>", text.upper() 
print "lower", "=>", text.lower() 
print "split", "=>", text.split() 
print "join", "=>", "+".join(text.split()) 
print "replace", "=>", text.replace("Python", "Perl") 
print "find", "=>", text.find("Python"), text.find("Perl") 
print "count", "=>", text.count("n")


