"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。
"""
"""
#五位数数字判断是否为回文数
num = int(input("请输入需要判断的一个五位数字："))
n = []
while num / 10 != 0:
    n.append(num%10)
    num = num//10
if n[0] == n[4] and n[1] == n[3]:
    print("这个数字是回文数！")
else:
    print("这个数字不是回文数！")
"""

#任意位数数字判断是否为回文数
num = int(input("请输入需要判断的数字："))
n = []
shi = True
while num / 10 != 0:
    n.append(num%10)
    num = num//10
for i in range(len(n)):
    if n[i] != n[-i-1]:
        shi = False
if shi:
    print("这个数字是回文数！")
else:
    print("这个数字不是回文数！")
    
