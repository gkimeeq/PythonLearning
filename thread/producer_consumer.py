#!/usr/bin/env python
# coding=utf-8

import multiprocessing

Lock可以避免访问资源时的冲突
Queue是多进程安全的队列，可以使用它来实现多进程之间的数据传递
Pipe实现管道模式下的消息发送与接收

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

python仅仅支持一个线程的运行
GIL：global interpreter lock,全局解释器锁

设置GIL->开始一个线程->A、执行一定量的任务B、程序主动让出控制(sleep等)->把线程设置为休眠状态->解锁GIL->循环->设置GIL

thread模块，threading模块，推荐使用threading，因为在thread模块中，需要自行管理线程与主线程之间同步的问题，
而在threading模块中，已经进行了相关的封装，不需要管同步的问题

队列：FIFO，LIFO
