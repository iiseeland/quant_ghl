# -*- coding: utf-8 -*-
'''
Created on 2018��5��10��

@author: isld
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ChinaBank = pd.read_csv("ChinaBank.csv", index_col="Date")
#print (ChinaBank)
ChinaBank.index = pd.to_datetime(ChinaBank.index)
plt.plot(ChinaBank.Close['2014'])


plt.show()


