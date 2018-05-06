# -*- coding:utf-8 -*-
# Example 1-25. 显式地访问 _ _builtin_ _ 模块中的函数

def open(filename, mode="rb"): 
    import __builtin__ 
    file = __builtin__.open(filename, mode) 
    if file.read(5) not in("GIF87", "GIF89"): 
        raise IOError, "not aGIF file" 
    
    file.seek(0) 
    return file 
    
fp = open("samples/sample.gif") 
print len(fp.read()), "bytes" 
 
fp = open("samples/sample.jpg") 
print len(fp.read()),  "bytes"


