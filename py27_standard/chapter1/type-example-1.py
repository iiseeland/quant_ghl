# -*- coding:utf-8 -*-
# Example 1-86. 使用 types 模块  
# File: types-example-1.py 
 
# 注意所有的类都具有相同的类型, 所有的实例也是一样. 要测试一个类或者实
# 例所属的类, 可以使用内建的 issubclass 和 isinstance 函数
 
import types 
 
def check(object): 
    print object, 
 
    if type(object) is types.IntType: 
        print "INTEGER", 
    if type(object) is types.FloatType: 
        print "FLOAT", 
    if type(object) is types.StringType: 
        print "STRING",     
    if type(object) is types.ClassType: 
        print "CLASS", 
    if type(object) is types.InstanceType: 
        print "INSTANCE", 
    print 
 
check(0) 
check(0.0) 
check("0") 
 
class A: 
    pass 
 
class B: 
    pass 
 
check(A) 
check(B) 
 
a = A() 
b = B() 
 
check(a) 
check(b)




