# -*- coding:utf-8 -*-
# Example 1-43. 使用 os.path 模块检查文件名的特征

import os 
 
FILES = ( 
    os.curdir, 
    "/", 
    "file", 
    "/file", 
    "samples", 
    "samples/sample.jpg",
    "directory/file", 
    "../directory/file", 
    "/directory/file" 
    ) 
 
for file in FILES: 
    print file, "=>", 
    if os.path.exists(file): 
        print "EXISTS", 
    if os.path.isabs(file): 
        print "ISABS", 
    if os.path.isdir(file): 
        print "ISDIR", 
    if os.path.isfile(file): 
        print "ISFILE", 
    if os.path.islink(file): 
        print "ISLINK", 
    if os.path.ismount(file): 
        print "ISMOUNT", 
    print


