"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析：无
"""


run = True
while run:
    n = int(input("请输入数字："))
    #定义一个匿名函数t
    t = lambda n : n**2>=50
    run = t(n)
    #三元操作符
    #run = True if n**2>=50 else False
    print("该数字的平方是：%d"%(n**2))
print("Done！")



"""
n = int(input("请输入数字："))
while n ** 2 >= 50:
    print("该数字的平方是：%d"%(n**2))
    n = int(input("请输入数字："))
print("该数字的平方是：%d"%(n**2))
print("Done！")
"""   
