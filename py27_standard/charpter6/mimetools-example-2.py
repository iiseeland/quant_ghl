# -*- coding:utf-8 -*-
# Example 6-3. 使用 mimetools 模块  
# File: mimetools-example-1.py 
 
import mimetools 
 
file = open("samples/sample.msg") 
 
msg = mimetools.Message(file) 
 
print "type", "=>", msg.gettype() 
print "encoding", "=>", msg.getencoding() 
print "plist", "=>", msg.getplist() 
 
print "header", "=>" 
for k, v in msg.items(): 
    print "  ", k, "=", v 




