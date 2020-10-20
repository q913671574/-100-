"""
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
"""

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cont = 0
#方法一：
"""
#遍历第一维
for i in range(3):
    #遍历第二维
    for n in range(3):
        if i == n:
            cont += a[i][n]
"""
#方法二:
#直接对对角线元素进行加和
for i in range(3):
    cont += a[i][i]

print(cont)
