# -*- coding:utf-8 -*-
# Example 1-55. 使用 re 模块抽出匹配的子字符串

import re 
 
text ="10/15/99" 
 
m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text) 
if m: 
    print m.group(1, 2, 3)


