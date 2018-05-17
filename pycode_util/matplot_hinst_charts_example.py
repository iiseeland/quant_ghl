# -*- coding: utf-8 -*-
'''
Created on 2018��5��12��

@author: isld
'''

# 直方图
import matplotlib_base_example as mb
import matplotlib.pyplot as plt

# plt.hist(x, bins, range, normed, weights, cumulative, bottom, histtype, align, orientation, rwidth, log, color, label, stacked, hold, data)

# plt.hist(mb.Close, bins=24)
# 水平直方图
# plt.hist(mb.Close, bins=12, orientation='horizontal')
# 累计直方图
plt.hist(mb.Close, bins=12, cumulative=True)
plt.show()