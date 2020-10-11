"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'
"""
s = input("请输入一串字符串：")
letters = 0
space = 0
digit = 0
others = 0
for i in s:
    if i == "\n":
        break
    elif i.isalpha():
        letters +=1
    elif i.isspace():
        space += 1
    elif i.isdigit:
        digit +=1
    else:
        others +=1

print("char = %d,space = %d,digit = %d,others = %d" % (letters,space,digit,others))
