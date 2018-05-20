# -*- coding: utf-8 -*-
'''
Created on 2018��5��12��

@author: isld
'''

# 饼图
import matplotlib_base_example as mb
import matplotlib.pyplot as plt
import numpy as np

# plt.pie(x, explode, labels, colors, autopct, pctdistance, shadow, labeldistance, startangle, radius, counterclock, wedgeprops, textprops, center, frame, hold, data)

#plt.pie(mb.a, labels=('(2,3]', '(3,4]', '(4,5]' '(5,6]'), colors=('b', 'g', 'r', 'c'), shadow = True)

# plt.boxplot(x, notch, labels)

prcData = mb.ChinaBank.iloc[:, 1:5]
data = np.array(prcData)
print ('this is data: => \n', data, sep='')
plt.boxplot(data, labels=('open', 'High', 'Low', 'Close'))
plt.title("box chart.")

plt.show()

fig = plt.figure()
## [左下角坐标，长宽] ,百分比
ax1 = fig.add_axes([0.1, 0.1, 0.3, 0.3])
ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

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
ax2.set_xticklabes(Open.index[:10], rotation = 25)
ax2.set_ylabel('open price')
ax2.set_ylim(2.4, 2.65)

















