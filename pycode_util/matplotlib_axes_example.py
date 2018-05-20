# -*- coding: utf-8 -*-
'''
Created on 2018��5��12��

@author: isld
'''

# 饼图
import matplotlib_base_example as mb
import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()
## [左下角坐标，长宽] ,百分比
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.3])
ax2 = fig.add_axes([0.1, 0.6, 0.8, 0.3])

Open = mb.ChinaBank.Open
Close = mb.ChinaBank.Close
ax1.plot(Close[:10])
ax2.plot(Open[:10])

ax1.set_title("close price")
ax1.set_xlabel('Date')
ax1.set_xticklabels(Close.index[:10], rotation=25)
ax1.set_ylabel('Close price')
ax1.set_ylim(2.4, 2.65)

ax2.set_title('open price')
ax2.set_xlabel('date')
ax2.set_xticklabels(Open.index[:10], rotation = 25)
ax2.set_ylabel('open price')
ax2.set_ylim(2.4, 2.65)

plt.show()


# param: 2*2 第n个子图
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)















