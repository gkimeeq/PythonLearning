#!/usr/bin/env python
# coding=utf-8

import threading
import time
import Queue


def producer(name, q):
    while True:
        item = u'产品 {}'.format(q.count)
        q.put(item)
        print u'{} 生产了{}\n'.format(name, item)
        q.count += 1
        time.sleep(1)
        if q.count > 10:
            break

def consumer(name, q):
    while True:
        item = q.get()
        print u'{} 消费了{}\n'.format(name, item)
        time.sleep(2)
        if q.count > 10:
            break

def run_producer_consumer():
    q = Queue.Queue(maxsize=20)
    q.count = 1
    p1 = threading.Thread(target=producer, args=(u'工厂1', q))
    p2 = threading.Thread(target=producer, args=(u'工厂2', q))
    c1 = threading.Thread(target=consumer, args=(u'老百姓1', q))
    c2 = threading.Thread(target=consumer, args=(u'老百姓2', q))
    c3 = threading.Thread(target=consumer, args=(u'老百姓3', q))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()
    p1.join()
    p2.join()
    c1.join()
    c2.join()
    c2.join()


if __name__ == '__main__':
    run_producer_consumer()

'''
工厂2 生产了产品 1

老百姓2 消费了产品 1

工厂1 生产了产品 2

老百姓3 消费了产品 2

工厂2 生产了产品 3

老百姓1 消费了产品 3

工厂1 生产了产品 4

老百姓2 消费了产品 4

工厂2 生产了产品 5

老百姓3 消费了产品 5

工厂1 生产了产品 6

老百姓1 消费了产品 6

工厂2 生产了产品 7

工厂1 生产了产品 8

老百姓2 消费了产品 7

工厂2 生产了产品 9

老百姓3 消费了产品 8

工厂1 生产了产品 10
'''
