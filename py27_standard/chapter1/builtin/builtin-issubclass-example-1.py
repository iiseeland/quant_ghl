# -*- coding:utf-8 -*-
# Example 1-16. 使用 issubclass 函数
# isinstance 可以接受任何对象作为参数, 而 issubclass 函数在接受非
# 类对象参数时会引发 TypeError 异常
class A: 
    pass 
 
class B: 
    pass 
 
class C(A): 
    pass 
 
class D(A, B): 
    pass 
 
def dump(object): 
    print object, "=>", 
    if issubclass(object, A): 
        print "A", 
    if issubclass(object, B): 
        print "B", 
    if issubclass(object, C): 
        print "C",     
    if issubclass(object, D): 
        print "D", 
    print 
 
dump(A) 
dump(B) 
dump(C) 
dump(D) 
dump(0) 
dump("string")


