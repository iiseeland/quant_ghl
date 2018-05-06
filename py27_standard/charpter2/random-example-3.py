# -*- coding:utf-8 -*-
# Example 2-32. 使用 random 模块生成高斯分布随机数  
# File: random-example-3.py 
 
import random 
 
histogram = [0] * 20 
 
# calculate histogram for gaussian 
# noise, using average=5, stddev=1 
for i in range(1000): 
    i = int(random.gauss(5, 1) * 2) 
    histogram[i] = histogram[i] + 1 
 
# print the histogram 
m = max(histogram) 
for v in histogram: 
    print "*" * (v * 50 / m)




