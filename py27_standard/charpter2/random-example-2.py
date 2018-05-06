# -*- coding:utf-8 -*-
# Example 2-30. 使用 random 模块从序列取出随机项  
#File: random-example-2.py 
 
import random 
 
# random choice from a list 
for i in range(5): 
    a = [1, 2, 3, 5, 9]
    print random.choice(a)
    random.shuffle(a)
    print "after shuffle", "=>", a




