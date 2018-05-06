# -*- coding:utf-8 -*-
# Example 1-4. 使用 _ _import_ _ 函数加载模块
import glob, os 
 
modules = [] 
 
# 匹配路径，查找模块
for module_file in glob.glob(r"D:\work\python\py27_standard\*-plugin.py"): 
    print module_file
    try: 
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        print os.path.basename(module_file)
        module = __import__(module_name) 
        modules.append(module) 
    except ImportError: 
        print ("err happen")
        #pass # ignore broken modules 
 
# say hello to all modules 
for module in modules: 
    module.hello()
