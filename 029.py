"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
"""
num = int(input("请输入需要分解的数字："))
n = []
while num%10 != 0:
    n.append(num%10)
    num = num//10

lenth = len(n)
print("该数字是%d位数字。"% lenth)
print("正序")
for i in n:
    print(i)
print("倒序1")
for i in range(len(n)-1, -1, -1):
    print(n[i])

print("倒序2")
for i in n[::-1]:
    print(i)
print("倒序3")
#逐个弹出n中最后一个元素
for i in range(len(n)):
    c = n.pop()
    print(c)
print(n)
