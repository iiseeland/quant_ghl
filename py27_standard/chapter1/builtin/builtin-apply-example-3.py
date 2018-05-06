#使用 apply 函数调用基类的构造函数
# 使用 * 来标记元组, ** 来标记字典
class Rectangle: 
    def __init__(self, color="white", width=10, height=10): 
        print "create a", color, self, "sized", width, "x", height 
 
class RoundedRectangle(Rectangle): 
    def __init__(self, **kw): 
        apply(Rectangle.__init__, (self,), kw) 
 
rect = Rectangle(color="green", height=100, width=100) 
rect = RoundedRectangle(color="blue",height = 20)