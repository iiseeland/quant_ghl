# -*- coding: utf-8 -*-
'''
Created on 2018年5月4日

@author: isld
'''

str1 = "Finace in python"
str1 = 'stock price of alibaba'
str1 = """'beauty' of pyton """
s = str(123455)
len(s)

s = "wOrdE"
print (s.capitalize())

s = "ThIs Is mY STRING Test"
print (s.title())

'''
str.islower()
str.isupper()
str.lower()
str.upper()
str.istitle()
str.title()        # 每个单词的首字母大写
str.capitalize()  # 整个字符串首字母大写
str.swapcase()    # 每个字符的大小写调换
'''

'''
str.find(x)
str.index(x)
str.rfine(x)
str.rindex(x)
str.startswith(x)
str.endswith(x)    # x如果是元组，则元组内的任意一个字符串符合条件都返回treue
str.strip([chars])
str.rstrip([char])
'''

s = 'Ia_xxx_db'
print(str.strip(s, "aIdb"))
print (s)
print (str.rstrip(s, "aIdb"))



GeogeSoros="""I' m only rich beause i know when I' m wrong, I basically
have survived by recgnizing my mistakes."""
print(GeogeSoros.split())
split_GS=GeogeSoros.split()
count_GS={}
for i in split_GS:
    #print (i)
    if "," in i:
        split_GS.remove(i);
        split_GS.append(i.split(",")[0])
    if '.' in i:
        split_GS.remove(i)
        split_GS.append(i.split('.')[0])
print ("split_GS ==> ", split_GS)    
for j in split_GS:
    count_GS[j] = split_GS.count(j)
    
print("count_GS ==>", count_GS)        