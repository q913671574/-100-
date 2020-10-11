"""
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘
"""
cont = 0
ji = 1
for i in range(1, 20):
    ji *= i
    cont += ji
print(cont)
