#!/usr/bin/env python
# coding=utf-8

import re


def simple_use():
    p = re.compile(r'abc')  # 返回一个pattern对象，匹配abc
    r1 = re.match(p, 'abc')
    r2 = re.match(p, 'abcc def')
    r3 = re.match(p, 'ac def')
    r4 = re.match(p, 'abc def')

    if r1:
        print r1.group()  # abc
    else:
        print u'r1失败'

    if r2:
        print r2.group()  # abc
    else:
        print u'r2失败'

    if r3:
        print r3.group()
    else:
        print u'r3失败'  # r3失败

    if r4:
        print r4.group()  # abc
    else:
        print u'r4失败'

    p = re.compile(r'\d+')  # 一个或多个数字
    s = 'a1b2c3'
    print re.split(p, s)  # ['a', 'b', 'c', '']
    print re.findall(p, s)  # ['1', '2', '3']
    for m in re.finditer(p, s):
        print m.group(),  # 1 2 3
    print

    p = re.compile(r'(\w+) (\w+)')  # 词+空格+词
    s = 'happy birthday to you!'
    print re.sub(p, r'\2 \1', s)  # birthday happy you to!
    print re.subn(p, r'\2 \1', s)  # ('birthday happy you to!', 2)
    def repl(m):
        return m.group(1).upper() + ' ' + m.group(2).upper()
    print re.sub(p, repl, s)  # HAPPY BIRTHDAY TO YOU!
    print re.subn(p, repl, s)  # ('HAPPY BIRTHDAY TO YOU!', 2)

    print re.escape('python.exe')  # python\.exe


def match_use():
    m = re.match(r'(\w+) (\w+)(?P<mark>.*)', 'hello world!')  # 匹配：词+空格+词+任意字符
    print 'm.string = ', m.string  # m.string =  hello world!
    print 'm.re = ', m.re  # m.re =  <_sre.SRE_Pattern object at 0x7f43473e8ad0>
    print 'm.pos = ', m.pos  # m.pos =  0
    print 'm.endpos = ', m.endpos  # m.endpos =  12
    print 'm.lastindex = ', m.lastindex  # m.lastindex =  3
    print 'm.lastgroup = ', m.lastgroup  # m.lastgroup =  mark
    print 'm.group() = ', m.group()  # m.group() =  hello world!
    print 'm.groups() = ', m.groups()  # m.groups() =  ('hello', 'world', '!')
    print 'm.groupdict() = ', m.groupdict()  # m.groupdict() =  {'mark': '!'}
    print 'm.start(1) = ', m.start(1)  # m.start(1) =  0
    print 'm.end(1) = ', m.end(1)  # m.end(1) =  5
    print 'm.start(2) = ', m.start(2)  # m.start(2) =  6
    print 'm.end(2) = ', m.end(2)  # m.end(2) =  11
    print 'm.span(1) = ', m.span(1)  # m.span(1) =  (0, 5)
    print 'm.span(2) = ', m.span(2)  # m.span(2) =  (6, 11)
    print r'm.expand(r"\2  \1\3") = ', m.expand(r'\2  \1\3')  # m.expand(r"\2  \1\3") =  world  hello!


# search和match的区别
def search_vs_match():
    p = re.compile(r'world')
    m = re.search(p, 'hello world')  # world不是在开头也能匹配到
    if m:
        print m.group()  # world

    m2 = re.match(p, 'hello world')  # world不是在开头，匹配不到
    if m2:
        print m2.group()
    else:
        print u'没有匹配'  # 没有匹配


if __name__ == '__main__':
    simple_use()
    print '*' * 100
    match_use()
    print '*' * 100
    search_vs_match()


'''
输出：

abc
abc
r3失败
abc
['a', 'b', 'c', '']
['1', '2', '3']
1 2 3
birthday happy you to!
('birthday happy you to!', 2)
HAPPY BIRTHDAY TO YOU!
('HAPPY BIRTHDAY TO YOU!', 2)
python\.exe
****************************************************************************************************
m.string =  hello world!
m.re =  <_sre.SRE_Pattern object at 0x7f43473e8ad0>
m.pos =  0
m.endpos =  12
m.lastindex =  3
m.lastgroup =  mark
m.group() =  hello world!
m.groups() =  ('hello', 'world', '!')
m.groupdict() =  {'mark': '!'}
m.start(1) =  0
m.end(1) =  5
m.start(2) =  6
m.end(2) =  11
m.span(1) =  (0, 5)
m.span(2) =  (6, 11)
m.expand(r"\2  \1\3") =  world  hello!
****************************************************************************************************
world
没有匹配
'''
