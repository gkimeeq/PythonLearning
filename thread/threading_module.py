#!/usr/bin/env python
# coding=utf-8

from threading import Thread
import time


def loop(name, seconds):
  print 'start loop', name, ' at:', time.ctime()
  time.sleep()
  print 'end loop', name, ' at:', time.ctime()
  
loops = [2, 4]
nloops = range(len(loops))
threads = []
print 'starting at :', time.ctime()
for i in nloops:
  t = Thread(target=loop, args=(i, loops[i]))
  threads.append(t)
for i in nloops:
  threads[i].start()
for i in nloops:
  threads[i].join()
print 'all done at:', time.ctime()
