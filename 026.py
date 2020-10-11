"""
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4！
"""
def fn(num):
    return 1 if num == 1 else fn(num-1)*num

"""
    if num == 1:
        return 1
    else:
        return fn(num-1)*num
"""

print(fn(5))
