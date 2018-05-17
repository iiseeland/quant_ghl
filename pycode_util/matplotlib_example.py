# -*- coding: utf-8 -*-
'''
Created on 2018

@author: isld
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Vera']

ChinaBank = pd.read_csv("ChinaBank.csv", index_col="Date")
#print (ChinaBank)
ChinaBank.index = pd.to_datetime(ChinaBank.index)
plt.plot(ChinaBank.Close['2014'], label='close price', marker = '>')
plt.plot(ChinaBank.Open['2014'], label='open price', ls= '-.', c='b', linewidth =2 )
# plt.plot(ChinaBank.Open['2014'],  '--b>', label = 'xxxx')
'''
plt.plot([1,1, 0, 0, -1, 0, 1, 1, -1])
# 设定x轴和y轴的范围
plt.ylim(-1.5, 1.5)
plt.xlim(-1, 9)


# 设定X和Y的标签
#plt.xticks(location, lables， rotation)
#plt.yticks(location, lables)
plt.xticks(range(9), \
           ['2015-01-02', '2015-01-03', \
            '2015-01-04',  '2015-01-05', \
            '2015-01-06',  '2015-01-07', \
            '2015-01-08',  '2015-01-09', \
            '2015-01-10'], rotation = 45)
'''

# 参数linestyle取值：
'''
实线 solid        '-'
虚线 dashed
线点 dashdot
点线 dotted
不画线 None
'''
# 添加标题
# plt.title(s, *args, **kwargs)
plt.title("china bank 2014 close line", loc = 'right') # loc:left, right, center
plt.xlabel('dates')
plt.ylabel('closes')

# b：是否显示
# which: 坐标轴分割标线的类型， major, minor, both
# axis： both, X ,Y
#plt.grid(b=None, which='major', axis='both', **kwargs)
plt.grid(True, axis='y')

# 图例
# 参数loc取值：
'''
0 best
1 upper right
2 upper left
3 lower left
4 lower right
5 right
6 center left
7 center right
8 lower center
9 upper center
10 center
'''
# plt.legend(*args, **kwargs)
plt.legend()


plt.show()


