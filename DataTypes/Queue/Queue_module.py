#!/usr/bin/env python
# coding=utf-8

import Queue
import time

'''
https://docs.python.org/2/library/queue.html

Queue模块在Python 3中改名为queue了。
Queue模块实现了多个生产者消费者列队，可以在多线程中进行安全的信息交换。
Queue模块定义了三个类：Queue.Queue, Queue.LifoQueue, Queue.PriorityQueue，还包含两个异常：Queue.Empty, Queue.Full。
'''

'''
exception Queue.Empty：
如果队列为空，使用非阻塞的方法获取队列的值，如get()或get_nowait()，则抛出此异常。
'''

'''
exception Queue.Full：
如果队列已满，使用非阻塞的方法插入值，如put()或put_nowait()，则抛出此异常。
'''

'''
Queue的方法：
qsize()：获取队列的大概容量，是大概容量！！！
empty()：是否空。
full()：是否满。
put(item[, block[, timeout]])：数据入队，默认block是True，timeout为None，队列满则阻塞；如果block为True，timeout > 0，则等待timeout秒，队列仍为满则抛Full异常；如果block为False，则队列满立刻抛Full异常。
put_nowait(item)：等同于put(item, block=False)。
get([block[, timeout]])：数据移出队列，默认block是True，timeout为None，队列空则阻塞；如果block为True，timeout > 0，则等待timeout秒，队列仍为空则抛Empty异常；如果block为False，则队列空立刻抛Empty异常。
get_nowait()：等同于get(block=False)。
task_done()：指示正常入队的数据任务已完成。在get()后再调用task_done()则告诉队列此项数据任务已完成。如果调用的次数比数据项的数目多，则抛出ValueError异常。
join()：队列一直阻塞，直到所有数据出列并处理。新入列数据项，总数据项增加1。当数据出列，处理完后调用task_done()则表示处理完毕，总数据项减1。
'''

'''
class Queue.Queue(maxsize=0)：
先入先出队列，maxsize是指定最大容量，如果为0或负值，则队列容量可以无穷大。队列满还插入则会阻塞。
'''
def operate_queue():
    q = Queue.Queue()
    print u'队列空吗？{0}'.format(q.empty())
    q.put('data1')
    q.put('data2')
    q.put('data3')
    print u'队列满吗？{0}'.format(q.full())
    print q.get()
    print q.get()
    print q.get()
    try:
        print u'时间点：{0}'.format(time.ctime())
        q.get(timeout=3)  # 阻塞3秒，然后抛Empty异常
    except Queue.Empty:
        print u'时间点：{0}'.format(time.ctime())
        print u'队列已经空了'

    try:
        print u'时间点：{0}'.format(time.ctime())
        q.get_nowait()  # 即刻抛Empty异常
    except Queue.Empty:
        print u'时间点：{0}'.format(time.ctime())
        print u'队列已经空了'

    try:
        print u'时间点：{0}'.format(time.ctime())
        q.get(block=False)  # 即刻抛Empty异常
    except Queue.Empty:
        print u'时间点：{0}'.format(time.ctime())
        print u'队列已经空了'

    print u'队列大概容量为：{0}'.format(q.qsize())

    q = Queue.Queue(maxsize=3)
    q.put('d1')
    q.put('d2')
    q.put('d3')
    try:
        print u'时间点：{0}'.format(time.ctime())
        q.put('d4', block=False)  # 即刻抛Full异常
    except Queue.Full:
        print u'时间点：{0}'.format(time.ctime())
        print u'队列已经满了'


'''
class Queue.LifoQueue(maxsize=0)：
后入先出队列，maxsize是指定最大容量，如果为0或负值，则队列容量可以无穷大。队列满还插入则会阻塞。
'''
def operate_lifoqueue():
    q = Queue.LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print q.get()
    print q.get()
    print q.get()


'''
class Queue.PriorityQueue(maxsize=0)：
优先队列，maxsize是指定最大容量，如果为0或负值，则队列容量可以无穷大。队列满还插入则会阻塞。
典型的队列数据为元组(priority_num, data)，优先值越小，优先级越高。
'''
def operate_priorityqueue():
    q = Queue.PriorityQueue()  # 数字小优先级高
    q.put((1, 'YaoMing'))
    q.put((-1, 'MaLong'))
    q.put((10, 'ZhengZhi'))
    q.put((5, 'ZhuTing'))
    print q.get()
    print q.get()
    print q.get()
    print q.get()


if __name__ == '__main__':
    print u'先进先出队列：'
    operate_queue()
    print '*' * 50
    print u'后进先出队列：'
    operate_lifoqueue()
    print '*' * 50
    print u'优先队列：'
    operate_priorityqueue()


'''
输出为：

先进先出队列：
队列空吗？True
队列满吗？False
data1
data2
data3
时间点：Thu Jun 27 16:33:27 2019
时间点：Thu Jun 27 16:33:30 2019
队列已经空了
时间点：Thu Jun 27 16:33:30 2019
时间点：Thu Jun 27 16:33:30 2019
队列已经空了
时间点：Thu Jun 27 16:33:30 2019
时间点：Thu Jun 27 16:33:30 2019
队列已经空了
队列大概容量为：0
时间点：Thu Jun 27 16:33:30 2019
时间点：Thu Jun 27 16:33:30 2019
队列已经满了
**************************************************
后进先出队列：
3
2
1
**************************************************
优先队列：
(-1, 'MaLong')
(1, 'YaoMing')
(5, 'ZhuTing')
(10, 'ZhengZhi')
'''
