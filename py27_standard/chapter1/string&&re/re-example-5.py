# -*- coding:utf-8 -*-
# Example 1-58. 使用 re 模块替换字符串(通过回调函数)

import re 
import string 
 
text = "a line of text\\012another line of text\\012etc..." 
 
def octal(match): 
    # replace octal code with corresponding ASCII character 
    # 使用对应 ASCII 字符替换八进制代码 
#    return chr(string.atoi(match.group(1), 8)) 
    return '++'
 
octal_pattern = re.compile(r"\\(\d\d\d)") 
 
print text 
print octal_pattern.sub(octal, text)


