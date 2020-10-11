"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""

import math
h=0

for i in range(101, 201):
    leap = 0
    s = int(math.sqrt(i))
    for m in range(2, s+1):
        #能被整除
        if i%m == 0:
            leap =1
            break
    #
    if leap == 0:
        h += 1
        print(i)

print("共有素数 %d" % h)
