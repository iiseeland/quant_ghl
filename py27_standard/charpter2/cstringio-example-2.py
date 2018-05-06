# -*- coding:utf-8 -*-
# Example 2-12. 后退至 StringIO  
# File: cstringio-example-2.py 
 
try: 
    import cStringIO 
    StringIO = cStringIO 
except ImportError: 
    import StringIO 
 
print StringIO




