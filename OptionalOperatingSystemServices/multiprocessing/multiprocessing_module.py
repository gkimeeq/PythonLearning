#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time
import os

'''
Python中的多线程并不是真正的多线程，是利用GIL（Global Interpreter Lock）来实现的多线程，本质上仍然是单线程。
如果想利用多个CPU的资源，Python中大部分情况需要使用多进程，multiprocessing模块提供了类似于多线程的API，可以完全利用多CPU资源。
'''

'''
进程类Process
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
group：保留为以后所用，用None即可
target：可调用目标，会在run()中调用
name：进程名，默认为Process-#
args：传入target的参数元组
kwargs：传入target的参数字典

属性：
name：进程名
daemon：是否为守护进程，要在start()之前设置才有效
pid：进程ID，在进程生成之前为None
exitcode：退出码，如还没终止，为None，由信号N终止，则为-N
authkey：验证密钥

方法：
start()：开始进程，进程开始后，会自动运行run()
run()：进程执行任务入口
join([timeout])：父进程要等待调用join的进程结束之后才能运行，或等待timeout时间
is_alive()：进程是否还活着
terminate()：终止进程
'''

# 1.单进程
# 定义一个进程要运行的任务
def target_1(interval):
    n = 3
    while n > 0:
        print u'时间点：{0}'.format(time.ctime())
        time.sleep(interval)  # 睡眠interval秒
        n -= 1

def process_target_1():
    p = multiprocessing.Process(target=target_1, args=(3,))
    p.start()
    print u'进程ID：{0}'.format(p.pid)
    print u'进程名：{0}'.format(p.name)
    print u'进程活着吗？{0}'.format(p.is_alive())
    p.join()


# 2.多进程
def task_1(interval):
    print u'任务1开始\n'
    time.sleep(interval)
    print u'任务1结束\n'

def task_2(interval):
    print u'任务2开始\n'
    time.sleep(interval)
    print u'任务2结束\n'


def task_3(interval):
    print u'任务3开始\n'
    time.sleep(interval)
    print u'任务3结束\n'

def process_multi_tasks():
    p1 = multiprocessing.Process(target=task_1, args=(3,))
    p2 = multiprocessing.Process(target=task_2, args=(2,))
    p3 = multiprocessing.Process(target=task_3, args=(1,))
    p1.start()
    p2.start()
    p3.start()
    print u'CPU数为：{0}'.format(multiprocessing.cpu_count())
    for p in multiprocessing.active_children():
        print u'子进程名：{0}，ID：{1}'.format(p.name, p.pid)
    p1.join()
    p2.join()
    p3.join()
    print u'多进程任务结束'


# 3.通过继承自定义进程类
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):  # 当start()被调用，run()会被自动调用
        n = 3
        while n > 0:
            print u'时间点：{0}'.format(time.ctime())
            time.sleep(self.interval)
            n -= 1

# 使用自定义进程类
def customized_process():
    p = ClockProcess(3)
    p.start()  # 自动调用run()
    p.join()


# 4.使用Lock进行进程间同步，避免资源访问的冲突
def use_lock_task(lock, num):
    lock.acquire()  # 获得锁
    print u'数字：{0}'.format(num)
    lock.release()  # 释放锁

def process_use_lock_task():
    lock = multiprocessing.Lock()
    for num in range(10):
        p = multiprocessing.Process(target=use_lock_task, args=(lock, num))
        p.start()
        p.join()


# 5.使用Queue实现多进程之间数据传递，Queue是多进程安全的队列
def use_queue_write_task(q):
    try:
        q.put([1, None, 'Good'], block=False)
    except:
        pass

def use_queue_read_task(q):
    try:
        print q.get(block=False)
    except:
        pass

def process_use_queue():
    q = multiprocessing.Queue()
    w = multiprocessing.Process(target=use_queue_write_task, args=(q,))
    r = multiprocessing.Process(target=use_queue_read_task, args=(q,))
    w.start()
    r.start()
    w.join()
    r.join()


# 6.使用Pipe可以建立一对连接对象，俩连接对象是双工工作的
def use_pipe_task(conn):
    conn.send(['circle', {'cx': 5}, {'cy': 3}, {'radius': 5}])
    conn.close()

def process_use_pipe():
    conn1, conn2 = multiprocessing.Pipe()
    p = multiprocessing.Process(target=use_pipe_task, args=(conn2,))
    p.start()
    print conn1.recv()
    p.join()

    conn3, conn4 = multiprocessing.Pipe()
    p2 = multiprocessing.Process(target=use_pipe_task, args=(conn3,))
    p2.start()
    print conn4.recv()
    p2.join()


# 7.使用Value或Array共享资源，共享的对象是进程安全的
def use_value_array_task(v, a):
    v.value = 3.1415926
    for i in range(len(a)):
        a[i] = a[i] * a[i]

def process_use_value_array():
    v = multiprocessing.Value('d', 0.)  # d是指double类型
    a = multiprocessing.Array('i', range(5))  # i是指有符号整数
    p = multiprocessing.Process(target=use_value_array_task, args=(v, a))
    p.start()
    p.join()
    print v.value
    print a[:]


# 8.服务进程，Manager可以控制一个持有Python对象的服务进程，可以允许其它进程通过代理来操纵这些对象。
# Manager支持的对象类型包括：list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value, Array
# 比直接用Value和Array更加灵活，支持的类型更多，但速度上会有一定的代价
def use_manager_task(d, l):
    d['pi'] = 3.1415926
    for i in range(len(l)):
        l[i] = l[i] * l[i]

def process_use_manager():
    m = multiprocessing.Manager()
    d = m.dict()
    l = m.list(range(5))
    p = multiprocessing.Process(target=use_manager_task, args=(d, l))
    p.start()
    p.join()
    print d
    print l


# 9.使用Pool工作进程池
def pool_task(x):
    return x * x

def process_pool():
    pool = multiprocessing.Pool(processes=3)  # 三个工作进程
    print pool.map(pool_task, range(10))
    for i in pool.imap_unordered(pool_task, range(10)):  # 乱序
        print i,
    print

    res = pool.apply_async(pool_task, (3,))  # 只运行一个进程
    print res.get(timeout=1)

    res = pool.apply_async(os.getpid, ())  # 只运行一个进程，异步运行os.getpid()
    print res.get(timeout=1)  # 进程的ID

    results = [pool.apply_async(os.getpid, ()) for _ in range(3)]
    print [res.get(timeout=1) for res in results]

    res = pool.apply_async(time.sleep, (10,))  # 一个进程睡眠10秒
    try:
        print res.get(timeout=1)
    except multiprocessing.TimeoutError:
        print u'TimeoutError异常！'


if __name__ == '__main__':
    print u'1.单进程：\n'
    process_target_1()
    print '*' * 50
    print u'2.多进程：\n'
    process_multi_tasks()
    print '*' * 50
    print u'3.通过继承自定义进程类:\n'
    customized_process()
    print '*' * 50
    print u'4.使用Lock进行进程间同步，避免资源访问的冲突:\n'
    process_use_lock_task()
    print '*' * 50
    print u'5.使用Queue实现多进程之间数据传递，Queue是多进程安全的队列:\n'
    process_use_queue()
    print '*' * 50
    print u'6.使用Pipe可以建立一对连接对象，俩连接对象是双工工作的:\n'
    process_use_pipe()
    print '*' * 50
    print u'7.使用Value或Array共享资源，共享的对象是进程安全的:\n'
    process_use_value_array()
    print '*' * 50
    print u'8.服务进程，Manager:\n'
    process_use_manager()
    print '*' * 50
    print u'9.使用Pool工作进程池:\n'
    process_pool()

    
'''
输出结果：

1.单进程：

进程ID：9200
进程名：Process-1
进程活着吗？True
时间点：Thu Jun 27 13:49:30 2019
时间点：Thu Jun 27 13:49:33 2019
时间点：Thu Jun 27 13:49:36 2019
**************************************************
2.多进程：

CPU数为：16
子进程名：Process-2，ID：10684
子进程名：Process-3，ID：7680
子进程名：Process-4，ID：5884
任务1开始

任务3开始

任务2开始

任务3结束

任务2结束

任务1结束

多进程任务结束
**************************************************
3.通过继承自定义进程类:

时间点：Thu Jun 27 13:49:42 2019
时间点：Thu Jun 27 13:49:45 2019
时间点：Thu Jun 27 13:49:48 2019
**************************************************
4.使用Lock进行进程间同步，避免资源访问的冲突:

数字：0
数字：1
数字：2
数字：3
数字：4
数字：5
数字：6
数字：7
数字：8
数字：9
**************************************************
5.使用Queue实现多进程之间数据传递，Queue是多进程安全的队列:

[1, None, 'Good']
**************************************************
6.使用Pipe可以建立一对连接对象，俩连接对象是双工工作的:

['circle', {'cx': 5}, {'cy': 3}, {'radius': 5}]
['circle', {'cx': 5}, {'cy': 3}, {'radius': 5}]
**************************************************
7.使用Value或Array共享资源，共享的对象是进程安全的:

3.1415926
[0, 1, 4, 9, 16]
**************************************************
8.服务进程，Manager:

{'pi': 3.1415926}
[0, 1, 4, 9, 16]
**************************************************
9.使用Pool工作进程池:

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
0 1 4 9 16 25 36 49 64 81
9
10916
[8416, 10916, 8416]
TimeoutError异常！
'''
