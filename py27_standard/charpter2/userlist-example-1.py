# -*- coding:utf-8 -*-
# Example 2-16. 使用 UserList 模块  
# File: userlist-example-1.py 
 
import UserList 
 
class AutoList(UserList.UserList): 
 
    def __setitem__(self, i, item): 
        if i == len(self.data): 
            self.data.append(item) 
        else: 
            self.data[i] = item 
 
list = AutoList() 
 
for i in range(10): 
    list[i] = i 
 
print list




