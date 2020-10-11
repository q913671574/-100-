"""
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

import re

#计算天数
def count_days(year, month, day):
    rn = False
    #每月天数--闰年or非闰年
    day1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0

    #判断闰年
    if (year % 4 == 0 and year %100 != 0) or (year %400 ==0):
        rn = True
    else:
        rn = False
    print(rn)

    #判断月份是否正确
    if month<12 and month>0:
        #闰年
        if rn:
            if (month == 2 and day>29) or (day>day2[month]):
                print("天数错误")
            else:
                #计算天数
                for i in range(month):
                    if month -1 == i :
                        days += day
                    else:
                        days += day2[i]
        #非闰年
        else:
            if (month == 2 and day>28) or (day>day1[month]):
                print("天数错误")
            else:
               for i in range(month):
                    if month -1 == i :
                        days += day
                    else:
                        days += day1[i]

    else:
        print("月份错误")
        
    return days

if __name__ == "__main__":
    """
    time = input("输入年月日：")
    regex1 = re.compile(r'(\d*)\.(\d+)\.(\d+)')
    regex2 = re.compile(r'(\d*)年(\d+)月(\d+)日')
    data = regex1.findall(time)
    if data[0] == "":
        data.regex2.findall(time)
    if data[0] == "":
        print("输入错误！")
    else:
        print(data)
        year = int(data[0][0])
        month = int(data[0][1])
        day = int(data[0][2])
        """
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日期："))
    days = count_days(year, month, day)
    print(days)
