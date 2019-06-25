#!/usr/bin/env python
# coding=utf-8

import time

# 当前时间的时间戳，1970纪元后经过的浮点秒数
t = time.time()
print t

# 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
zone = time.altzone
print zone


# time.struct_time(tm_year=2019, tm_mon=6, tm_mday=25, tm_hour=20, tm_min=56, tm_sec=14, tm_wday=1, tm_yday=176, tm_isdst=0)
# 4位年数，月（1-12)，日（1-31)，小时（0-23)，分钟（0-59)，秒（0-61,60和61是闰秒），一周的第几日（0-6,0是星期一），
# 一年的第几日（1-366)，夏令时（-1,0,1,-1是决定是否是夏令时的旗帜）
lt = time.localtime(t)
print lt

# 接受时间元组并返回一个可读的形式为“Tue Dec 11 18:07:14 2008" (2008年12月11日周二18时07分14秒）的24个字符的字符串。接收时间元组
print time.asctime(lt)
# 作用相当于time.asctime()，但接收时间戳
print time.ctime(t)

# 接受元组返回时间戳，会忽略毫秒
tt = time.mktime(lt)
print tt

# 返回格林威治天文时间下的时间元组
print time.gmtime(t)

# 用以浮点数计算的秒数返回当前的CPU时间，用来衡量不同程序的耗时比time.time()更有用
print time.clock()
# 推迟指定秒数调用线程的运行
time.sleep(5)
print time.clock()
time.sleep(5)
print time.clock()

# 以指定格式显示时间元组
s = time.strftime('%Y-%m-%d %H:%M:%S', lt)
print s
# 根据格式把时间字符串解析为时间元组，
lt = time.strptime(s, '%Y-%m-%d %H:%M:%S')
print lt
