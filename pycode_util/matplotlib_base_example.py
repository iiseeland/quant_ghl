# -*- coding: utf-8 -*-
'''
Created on 2018��5��12��

@author: isld
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Vera']

ChinaBank = pd.read_csv("ChinaBank.csv", index_col="Date")
#print (ChinaBank)
ChinaBank.index = pd.to_datetime(ChinaBank.index)
Close = ChinaBank.Close

print (Close.describe())
a = [0,0,0,0]
for i in Close:
    c = i
    if (c > 2) & (c <= 3):
        a[0] += 1
    elif (c > 3) & (c <= 4):
        a[1] += 1
    elif (c > 4) & (c <= 5):
        a[2] += 1
    else:
        a[3] += 1
print (a)

