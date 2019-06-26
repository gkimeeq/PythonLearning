#!/usr/bin/env python
# coding=utf-8

import multiprocessing

Queue是多进程安全的队列，可以使用它来实现多进程之间的数据传递

def writer_proc(q):
