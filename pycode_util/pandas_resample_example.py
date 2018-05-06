# -*- coding: utf-8 -*-
'''
Created on 2018年5月5日

@author: isld
'''
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=9, freq='T')
series = pd.Series(range(1,10), index=index)
print ("series => \n", series)

print ("series.resample('3T').first() =>\n", series.resample("3T").first())
print ("series.resample('3T').sum() =>\n", series.resample("3T").sum())

print ("series.resample('3T', label='right').first() =>\n", series.resample('3T', label='right').first())

print ("series.resample('3T', label='right', closed='right').sum() =>\n", \
       series.resample('3T', label='right', closed='right').sum())
print ("series.resample('3T', label='left', closed='right').sum() =>\n", \
       series.resample('3T', label='left', closed='right').sum())
