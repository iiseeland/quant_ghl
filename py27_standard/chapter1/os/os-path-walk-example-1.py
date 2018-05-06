# -*- coding:utf-8 -*-
# Example 1-46. 使用 os.path 搜索文件系统
# walk 函数会帮你找出一个目录树下的所有文件. 它的参数依次是目录名, 回调函数, 以及传递给回调函数的数据对象.

import os 
 
def callback(arg, directory, files): 
    for file in files: 
        print os.path.join(directory, file), repr(arg) 
 
def callback2(arg, directory, files):
    for file in files:
        if file == "os-path-walk-example-1.py":
            print "file the file: ", os.path.join(directory, file)
            break
 
os.path.walk("d:/", callback2, "secret message") 

