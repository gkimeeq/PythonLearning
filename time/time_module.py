#!/usr/bin/env python
# coding=utf-8

import time

t = time.time()
print t

zone = time.altzone
print zone

lt = time.localtime(t)
print lt

tt = time.mktime(lt)
print tt

print time.clock()
time.sleep(5)
print time.clock()
time.sleep(5)
print time.clock()

s = time.strftime('%Y-%m-%d %H:%M:%S', lt)
print s
lt = time.strptime(s, '%Y-%m-%d %H:%M:%S')
print lt
