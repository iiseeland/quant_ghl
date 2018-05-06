﻿# -*- coding:utf-8 -*-
# Example 1-49. 使用 DirectoryStatWalker 搜索文件系统

import os, stat 
 class DirectoryStatWalker: 
    # a forward iterator that traverses a directory tree, and 
    # returns the filename and additional file information 
 
    def _ _init_ _(self, directory): 
        self.stack = [directory] 
        self.files = [] 
        self.index = 0 
 
    def _ _getitem_ _(self, index): 
        while 1: 
            try: 
                file = self.files[self.index] 
                self.index = self.index + 1 
            except IndexError: 
                # pop next directory from stack 
                self.directory = self.stack.pop() 
                self.files = os.listdir(self.directory) 
                self.index = 0 
            else: 
                # got a filename 
                fullname = os.path.join(self.directory, file) 
                st = os.stat(fullname) 
                mode = st[stat.ST_MODE] 
                if stat.S_ISDIR(mode) and not stat.S_ISLNK(mode): 
                    self.stack.append(fullname) 
                return fullname, st 
 
for file, st in DirectoryStatWalker("."): 
    print file, st[stat.ST_SIZE]


