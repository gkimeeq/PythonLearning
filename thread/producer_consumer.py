#!/usr/bin/env python
# coding=utf-8

import multiprocessing

Queue是多进程安全的队列，可以使用它来实现多进程之间的数据传递

def writer_proc(q):
  try:
    q.put(1, block=False)
  except:
    pass
  
  
def reader_proc(q):
  try:
    print q.get(block=False)
  except:
    pass
  
  
q = multiprocessing.Queue()
writer = multiprocessing.Process(target=writer_proc, args=(q,))
writer.start()
reader = multiprocessing.Process(target=reader_proc, args=(q,))
reader.start()
reader.join()
writer.join()
