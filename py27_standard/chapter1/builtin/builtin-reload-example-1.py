# -*- coding:utf-8 -*-

#Example 1-8. 使用 reload 函数
# 已经用原模块里的类建立的实例仍然使用的是老模块(不会被更新)
# 使用 from-import 直接创建的到模块内容的引用也是不会被更新的
import hello 
reload(hello) 
reload(hello) 
hello.hello()