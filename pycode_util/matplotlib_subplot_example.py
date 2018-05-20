# -*- coding: utf-8 -*-
'''
Created on 2018��5��12��

@author: isld
'''

# 饼图
import matplotlib_base_example as mb
import matplotlib.pyplot as plt
import numpy as np



# param: 2*2 第n个子图
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

Close15 = mb.ChinaBank.Close['2015']
ax1.plot(Close15, color = 'b')
ax1.set_ylabel('close price')
ax1.set_title("China bank 2015 close chart.")


Volume15 = mb.ChinaBank.Volume['2015']
Open15 = mb.ChinaBank.Open['2015']
ax2.plot(Volume15, )

left1 = Volume15.index[Close15 >= Open15]
high1 = Volume15[left1]
ax2.bar(left1, high1, color='r')
left2 = Volume15.index[Close15 < Open15]
high2 = Volume15[left2]
ax2.bar(left2, high2, color='g')
ax2.set_ylabel('volume')
ax2.set_title('China bank 2015 volume')



High15 = mb.ChinaBank.High['2015']
Low15 = mb.ChinaBank.Low['2015']
ax3.plot(Close15, label = "close price")
ax3.plot(Open15, '--*', label = 'open price')
ax3.plot(High15, '-+', label = 'High price')
ax3.plot(Low15, "-.>", label = 'Low price')
ax3.legend(loc = 'best')

plt.show()










