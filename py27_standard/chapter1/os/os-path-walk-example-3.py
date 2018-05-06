# -*- coding:utf-8 -*-
# Example 1-48. 使用 DirectoryWalker 搜索文件系统

import os 
 
class DirectoryWalker: 
    # a forward iterator that traverses a directory tree 
     def __init__(self, directory): 
        self.stack = [directory] 
        self.files = [] 
        self.index = 0 
 
    def __getitem__(self, index): 
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
                if os.path.isdir(fullname) and not os.path.islink(fullname): 
                    self.stack.append(fullname) 
                return fullname 
 
for file in DirectoryWalker("."): 
    print file


