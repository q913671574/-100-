"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。
"""

zi=2.0
mu=1.0
l=[]
cont=0
for i in range(20):
    l.append(zi/mu)
    zi,mu = zi+mu, zi
for i in l:
    cont += i
print(cont)
