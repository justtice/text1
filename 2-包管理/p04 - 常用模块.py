import  calendar

help(calendar.calendar)
# w = 每个日期的间隔字符数, l = 每周的间隔, c = 每月之间的间隔
cal = calendar.calendar(2018)
print(type(cal))

#是否是闰年
print (calendar.isleap(2018))
#
m3 = calendar.month(2018,8)
# print(m3)


print("**"*20)
import time
'''
时间元祖
引值（Index） 属性（Attribute） 值（Values）
0 tm_year（年） （例如：2015）
1 tm_mon（月） 1 ~ 12
2 tm_mday（日） 1 ~ 31
3 tm_hour（时） 0 ~ 23
4 tm_ （分） 0 ~ 59
5 tm_sec（秒） 0 ~ 61  (60表示闰秒,61保留值)
6 tm_wday（星期几） 0 ~ 6（0 表示星期一）
7 tm_yday（一年中的第几天） 1 ~ 366
8 tm_isdst（是否为夏令时） 0， 1， -1（-1 代表夏令时）
'''
#  time
### 时间戳   1970年1月1日0时0分到现在所经历的秒数

#时间模块的属性
# timezone : 当前系统的时区跟UTC时区的秒数   东八区  -28800秒
print (time.timezone)

t1 = time.time()  # 时间戳

print(time.localtime())
print(time.asctime())
print(time.ctime())  #当前时间的字符串化

tt =time.clock() # 运行时间,但3.6以后就不好用了
'''
localtime/gmtime 将时间戳转化为结构化时间

mktime 将结构化时间转化为时间戳
'''
# t2 = t1.localtime()
# print(t2)