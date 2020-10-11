"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数
"""
import time

l = ['1','2','3','4','5','6']
for i in range(len(l)):
    print (l[i])
    time.sleep(1)
