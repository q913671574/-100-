"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：无
"""
def down(num):
    return num/2

m = 100
cont=0
for i in range(10):
    cont += 1.5*m
    m /=2
print(cont)
print(m)
