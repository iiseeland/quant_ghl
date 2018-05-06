# -*- coding:utf-8 -*-
# Example 1-21. 执行已编译的代码

BODY = """ 
print 'the ant, an introduction' 
""" 
 
code =  compile(BODY,"<script>", "exec") 
 
print code 
 
exec code


