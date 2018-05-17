# -*- coding: utf-8 -*-
'''
Created on 2018��5��12��

@author: isld
'''

# 柱状图
import matplotlib_base_example as mb
import matplotlib.pyplot as plt



plt.title("china bank close graph")

# matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None,**kwargs)
# plt.barh(bottom, width, height, left, hold)
# plt.bar([2,3,4,5], mb.a)
plt.bar([2,3,4,5], mb.a, bottom=40.0)
plt.show()

