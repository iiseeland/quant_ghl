# -*- coding:utf-8 -*-
# Example 1-32. 使用 os 模块获取文件属性

import os 
import time 
 
file = "samples/sample.jpg" 
 
def dump(st): 
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st 
    print "- size:", size, "bytes" 
    print "- owner:", uid, gid 
    print "- created:", time.ctime(ctime) 
    print "- last accessed:", time.ctime(atime) 
    print "- last modified:", time.ctime(mtime) 
    print "- mode:", oct(mode) 
    print "- inode/dev:", ino, dev 
 
# 
# get stats for a filename 
st = os.stat(file) 
print  "stat", file 
dump(st) 
print # # get stats for an open file 
fp = open(file) 
st = os.fstat(fp.fileno()) 
print  "fstat",file 
dump(st)


