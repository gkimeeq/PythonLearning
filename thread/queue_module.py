#!/usr/bin/env python
# coding=utf-8

import queue


q = queue.Queue()
print q.empty()
q.put('d1')
q.put('d2')
q.put('d3')
print q.full()
print q.get()
print q.get()
print q.get()
print q.get(timeout=1) # 阻塞，用timeout设置超时解决阻塞问题，抛出queue.Empty异常
print q.get_nowait()  # 设置不等待，没有数据即刻抛出异常
print q.qsize()
print q.get(block=False) # block参数False也可以解决程序阻塞问题

q = queue.Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)
q.put(4, block=False) # 阻塞

q = queue.PriorityQueue() # 数字小优先级高
q.put((1, 'King'))
q.put((-1, 'Jeson'))
q.put((10, 'Tim'))
q.put((5, 'Mike'))

q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print q.get()
print q.get()
print q.get()
