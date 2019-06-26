#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time

python中的多线程并不是真正的多线程，如果想要利用多CPU的资源，python中大部分情况需要需要使用多进程。模拟了多线程，实质还是单线程。

进程类Process
is_alive()
join()
run()
start()

def worker(interval):
  n = 5
  while n > 0:
    print 'The time is {0}'.format(time.ctime())
    time.sleep(interval)
    n -= 1
    
    
单进程
if __name__ == '__main__':
  p = multiprocessing.Process(target=worker, args=(3,))
  p.start()
  print 'p.pid:', p.pid
  print 'p.name:', p.name
  print 'p.is_alive:', p.is_alive()

  
多进程
def worker_1(interval):
  print 'worker_1'
  time.sleep(interval)
  print 'end worker_1'
  
  
def worker_2(interval):
  print 'worker_2'
  time.sleep(interval)
  print 'end worker_2'
  
  
def worker_3(interval):
  print 'worker_3'
  time.sleep(interval)
  print 'end worker_3'
  
  
p1 = multiprocessing.Process(target=worker_1, args=(2,))
p2 = multiprocessing.Process(target=worker_2, args=(3,))
p3 = multiprocessing.Process(target=worker_3, args=(4,))
p1.start()
p2.start()
p3.start()
print 'The number of cpu is ' + str(multiprocessing.cpu_count())
for p in multiprocessing.active_children():
  print 'child p.name:', p.name, '\tp.id:', p.pid
print 'End!!!'
