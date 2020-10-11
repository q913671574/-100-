"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
"""
"""
s = ("")
n = ("")
c = int(input("循环次数："))
for i in range(c-1):
    n = ("")
    for m in range(i+1):
        n += "2"
    s += n + "+"
n = ("")
for m in range(i+1):
    n += "2"
    s += n 

print(s)
"""

s = 0
n = ("")
c = int(input("循环次数："))
for i in range(c):
    n = ("")
    for m in range(i+1):
        n += "2"
    s += int(n)

print(2+22+222+2222+22222) #循环5次
print(s)
