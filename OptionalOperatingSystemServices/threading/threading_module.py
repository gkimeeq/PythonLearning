#!/usr/bin/env python
# coding=utf-8

import threading
import time

'''
Python中的多线程并不是真正的多线程，是利用GIL（Global Interpreter Lock，全局解释器锁）来实现的多线程，本质上仍然是单线程。
GIL的工具流程是：
设置GIL->开始一个线程->执行一定量的任务，然后程序主动让出控制权（sleep等）->把线程设置为休眠状态->解锁GIL->如此循环回到开始的设置GIL
Python的多线程模块有thread和threading，推荐使用threading。因为在thread模块中，线程与主线程之间的同步问题要自行管理。
在threading模块中，这些同步问题已经作好了相关的封装，不需要管理同步问题。
'''

'''
https://docs.python.org/2/library/threading.html

threading模块中提供的函数有：
threading.active_count()， threading.activeCount()：返回活着的线程数，数值上等于enumerate()返回的列表的长度。
threading.Condition()：工厂函数，返回一个条件变量对象。条件变量允许一个或多个线程处于等待状态，直到被其它线程唤醒。
threading.current_thread()，threading.currentThread()：返回当前线程对象。如果调用者的线程控制不是由threading创建的，则会创建一个功能有限的虚拟线程。
threading.enumerate()：返回活着的线程对象列表，包括守护线程、虚拟线程（由current_thread()产生的）和主线程。已经终止的线程和未开始的线程排除在外。
threading.Event()：返回一个事件对象。
threading.Lock()：返回原始锁对象。如有线程获取了它，此后想再获取的都会处于阻塞，直到它被释放。任意线程都可以释放它。
threading.RLock()：返回可重获锁对象（Reentrant Lock Object）。要释放它，只能由获取它的线程来释放。同一线程可以再次获取而不会阻塞，但获取了多少次就要有多少次释放的动作。
threading.Semaphore([value])：返回信号量对象。信号量管理一个计数量，这个计数量是调用release()的次数减去调用acquire()的次数再加上一个初始值value（默认为1）。如果计数器为负值，acquire()在必要时会阻塞。
threading.BoundedSemaphore([value])：返回有界的信号量对象。有界信号量是用于当前值不超过初始值（默认为1）。如果超过，抛出ValueError异常。大多数情况，信号量是用来保证资源的有限容量，如果信号量被释放次数过多，就有bug的迹象。
threading.settrace(func)：为所有由threading创建的线程添加追踪函数。追踪函数func会在每个线程调用run()之前传递给 sys.settrace()。
threading.setprofile(func)：为所有由threading创建的线程添加配置函数。配置函数func会在每个线程调用run()之前传递给 sys.setprofile()。
threading.stack_size([size])：返回当新建线程时的堆栈大小。如果指定size，由此size用于后续创建的线程。size的值必须为0或一个大于32768（32KB）的整数。32KB是GIL自身得到保证的最小堆栈空间。如果size指定了一个不支持的值，抛出ThreadError异常；如果size无效，抛出ValueError异常。
'''

'''
threading模块中提供的类有：
class threading.local：线程局部数据类。使用时实例化一个对象，然后保存属性到这个对象。保存的属性对不同的线程是独立存在的。
class threading.Thread：线程控制类。
class threading.Timer：也是一个线程类，用于在指定时间后执行指定函数。
class threading.Lock：原始锁类。
class threading.RLock：可重获锁类。
class threading.Condition：条件变量类。
class threading.Semaphore：信号量类。
class threading.BoundedSemaphore：有界信号量类。
class threading.Event：事件类。
'''

'''
线程异常：
exception threading.ThreadError：线程相关的异常。很多接口使用RuntimeError，而不是ThreadError。
'''

'''
线程类Thread
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
group：保留为以后所用，用None即可
target：可调用目标，会在run()中调用
name：进程名，默认为Thread-#
args：传入target的参数元组
kwargs：传入target的参数字典

属性：
name：线程名，多个线程可能同名
daemon：是否为守护线程，要在start()之前设置才有效
ident：线程标识，如线程未开始则为None

方法：
start()：开始线程，线程开始后，会自动运行run()
run()：线程执行任务入口
join([timeout])：父线程要等待调用join的线程结束之后才能运行，或等待timeout时间
is_alive()，isAlive()：线程是否还活着
getName()：返回线程名
setName()：设置线程名，参考name属性
isDaemon()：是否为守护线程
setDaemon()：设置守护线程，参考daemon属性
'''
def loop_thread(name, sec):
    print u'开始循环{} 时间点：{}\n'.format(name, time.ctime())
    time.sleep(sec)
    print u'循环结束{} 时间点：{}\n'.format(name, time.ctime())


def run_loop_thread():
    loops = ['A', 'B']
    ts = [3, 5]
    n = len(loops)
    threads = []
    print u'所有线程开始时间：{}\n'.format(time.ctime())
    for i in range(n):
        t = threading.Thread(target=loop_thread, args=(loops[i], ts[i]))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print u'所有线程结束时间：{}'.format(time.ctime())


'''
原始锁类Lock

方法：
Lock.acquire([blocking])：获取锁，blocking为True时，获取不到则阻塞，直到获得为止
Lock.release()：释放锁
'''

'''
可重获取锁类RLock

方法：
RLock.acquire([blocking])：获取锁，blocking为True时，获取不到则阻塞，直到获得为止。如果当前线程已经拥有锁，再去获取，再增加锁的递归层数
RLock.release()：释放锁，减少递归层数
'''

'''
条件Condition
class threading.Condition([lock])
lock：如果为None，则新建一个Lock或RLock对象作为底层的锁

方法：
acquire(*args)：获取底层锁
release()：释放底层锁
wait([timeout])：线程等待此条件直到被唤醒或timeout时间到
notify(n=1)：唤醒n个等待此条件的线程
notify_all()，notifyAll()：唤醒所有等待此条件的线程
'''

'''
信号量类Semaphore
class threading.Semaphore([value])
value：内部计数器的初始值，默认为1。给0的话，抛出ValueError异常

方法：
acquire([blocking])：获取信号量
release()：释放信号量，内部计数器加1，
'''

'''
事件类Event
class threading.Event
线程简单的通过机制。一个线程发出事件信号，另一个线程等待事件信号。内部标帜初始为False

方法：
is_set()，isSet()：当内部标帜为True时返回True
set()：设置内部标帜为True
clear()：设置内部标帜为False
wait([timeout])：等待直到内部标帜为True，或timeout时间到。
'''

'''
计时器类Timer
class threading.Timer(interval, function, args=[], kwargs={})
interval：计时时间，单位为秒
function：执行的函数
args：function的列表参数
kwargs：function的字典参数

方法：
cancel()：停止计时器
'''


if __name__ == '__main__':
    run_loop_thread()

'''
输出为：

所有线程开始时间：Fri Jun 28 10:07:43 2019

开始循环A 时间点：Fri Jun 28 10:07:43 2019

开始循环B 时间点：Fri Jun 28 10:07:43 2019

循环结束A 时间点：Fri Jun 28 10:07:46 2019

循环结束B 时间点：Fri Jun 28 10:07:48 2019

所有线程结束时间：Fri Jun 28 10:07:48 2019
'''
