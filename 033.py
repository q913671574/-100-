"""
题目：按逗号分隔列表。

程序分析：无。
"""
n = ["1","2","3","4","5","6"]
#方法一：
c = ""
for i in range(1, len(n)):
    c += str(i) + ","
c += str(n[-1])
print(c)

#方法二：(此方法只使用于纯字符列表，无法应用于含有int型数据的列表)
s1 = ",".join(n)
print(s1)
