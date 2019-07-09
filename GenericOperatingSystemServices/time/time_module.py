#!/usr/bin/env python
# coding=utf-8

# 导入时间模块，Python自带，不用额外安装
import time

'''
https://docs.python.org/2/library/time.html

用到的时间元组
class time.struct_time
属性包括：
tm_year：4位数的年份
tm_mon：第几月（1-12）
tm_mday：每月第几天（1-31）
tm_hour：小时（0-23）
tm_min：分钟（0-59）
tm_sec：秒（0-61，当取值60或61时表示闰秒）
tm_wday：周的第几天（0-6，星期一是0）
tm_yday：年的第几天（1-366）
tm_isdst：夏令时（-1，0，1，其中-1是决定是否是夏令时的旗帜）
'''

# 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
zone = time.altzone
print zone
#  输出为：-32400

# 返回格林威治西部非夏令时地区的偏移秒数（大部分西欧为负值，美国为正值，英国为0）
tz = time.timezone
print tz
# 输出为：-28800

# 返回两个字符串的元组，第一个是非夏令时时区的名字，第二个是夏令时时区的名字，如果非夏令时时区没有定义，第二个字符串不应该被使用
tzn = time.tzname
print tzn
# 输出为：('China Standard Time', 'China Daylight Time')

# 重置转换规则
# time.tzset()
# 在Unix系统下才有

# 是否定义了夏令时时区，返回非零则为已定义
dst = time.daylight
print dst
# 输出为：0

# 是否接受两位数字的年份
a2 = time.accept2dyear
print a2
# 输出为：1

# 当前时间的时间戳，即1970纪元后经过的浮点秒数
t = time.time()
print t
# 输出为：1561509298.05  注意：当前时间不同，具体值会不一样

# 接受时间戳并返回一个24个字符的可读形式的字符串
ct = time.ctime(t)
print ct
# 输出为：Wed Jun 26 08:34:58 2019
print time.ctime()  # 不传入时间戳，则获取当前时间
# 输出为：Wed Jun 26 08:55:07 2019

# 接受时间戳，返回时间戳对应的时间元组
lt = time.localtime(t)
print lt
# 输出为：time.struct_time(tm_year=2019, tm_mon=6, tm_mday=26, tm_hour=8, tm_min=34, tm_sec=58, tm_wday=2, tm_yday=177, tm_isdst=0)
print time.localtime()  # 不传入时间戳，则获取当前时间
# 输出为：time.struct_time(tm_year=2019, tm_mon=6, tm_mday=26, tm_hour=9, tm_min=0, tm_sec=9, tm_wday=2, tm_yday=177, tm_isdst=0)

# 接受时间元组并返回一个24个字符的可读形式的字符串
at = time.asctime(lt)
print at
# 输出为：Wed Jun 26 08:34:58 2019
print time.asctime()  # 不传入时间元组，则获取当前时间
# 输出为：Wed Jun 26 09:03:24 2019

# 接受元组返回时间戳，会忽略毫秒
mt = time.mktime(lt)
print mt
# 输出为：1561509298.0

# 返回格林威治天文时间下的时间元组
gt = time.gmtime(t)
print gt
# 输出为：time.struct_time(tm_year=2019, tm_mon=6, tm_mday=26, tm_hour=0, tm_min=34, tm_sec=58, tm_wday=2, tm_yday=177, tm_isdst=0)
print time.gmtime()  # 不传入时间戳，则获取当前时间
# 输出为：time.struct_time(tm_year=2019, tm_mon=6, tm_mday=26, tm_hour=1, tm_min=6, tm_sec=37, tm_wday=2, tm_yday=177, tm_isdst=0)

# 用以浮点数计算的秒数返回当前的CPU时间，用来衡量不同程序的耗时比time.time()更有用
print time.clock()
# 输出为：2.84978877366e-07
# 推迟指定秒数再执行下一行命令
time.sleep(5)
print time.clock()
# 输出为：5.431048221
time.sleep(5)
print time.clock()
# 输出为：10.431552633

# 以指定格式的字符串显示时间元组
s = time.strftime('%Y-%m-%d %H:%M:%S', lt)
print s
# 输出为：2019-06-26 08:34:58
# 根据格式把时间字符串解析为时间元组
lt2 = time.strptime(s, '%Y-%m-%d %H:%M:%S')
print lt2
# 输出为：time.struct_time(tm_year=2019, tm_mon=6, tm_mday=26, tm_hour=8, tm_min=34, tm_sec=58, tm_wday=2, tm_yday=177, tm_isdst=-1)
'''
可用的格式符包括：
%a：星期的简短名称，如Wed
%A：星期的全名，如Wednesday
%b：月的简短名称，如Jun
%B：月的全名，如June
%c：适当的日期时间表达式，如06/26/19 08:34:58
%d：月的第几天（01-31），如26
%H：24小时制的小时（00-23），如08
%I：12小时制的小时（01-12），如08
%j：年的第几天（001-366），如177
%m：第几月（01-12），如06
%M：分钟（00-59），如34
%p：显示AM或PM
%S：秒（00-61），如58
%U：年的第几周（00-53），周日是周的第一日，新的一年中，第一个周日前的所有天都被归到第00个周中，如25
%w：星期几（0，6），0为周日，如3
%W：年的第几周（00-53），周一是周的第一日，新的一年中，第一个周一前的所有天都被归到第00个周中，如25
%x：适当的日期表达式，如06/26/19
%X：适当的时间表达式，如08:34:58
%y：去掉世纪的年的表示（00-99），即两位年的表示，如19
%Y：包括世纪的年的表示，即四位年的表示，如2019
%Z：时区名称，如果时区不存在，则为空，如China Standard Time
%%：“%”字符
'''
