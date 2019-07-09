#!/usr/bin/env python
# coding=utf-8

import urllib

'''
urllib模块：https://docs.python.org/2/library/urllib.html

urllib.urlopen(url[, data[, proxies[, context]]])：通过URL打开网络对象。如果没有指定模式标识符，或模式标识符为file:，将会打开一个本地文件，否则打开一个网络服务器套接字。
如果出错，抛出IOError异常。如果正常，返回一个类似文件的对象，这个对象的方法有：read(), readline(), readlines(), fileno(), close(), info(), getcode()和geturl()。
参数：data：http，POST请求的数据，需要urlencode()编码。proxies：代理字典，如果为空字典，则不用代理，如果为None，则用环境中的代理。context：可能为ssl.SSLContext的实例，配置SSL，用于HTTPS连接。
urllib.urlretrieve(url[, filename[, reporthook[, data[, context]]]])：复制URL的网络对象到本地。返回值为(filename,header)元组。
参数：filename：指定复制到本地的文件名。reporthook：指定一个回调函数，会在建立连接时和读取每个数据块后调用，这个回调函数被传入三个参数，第一个是已传输的数据块数，第二个是一个数据块的字节数，第三个是文件的总大小。data和context：与urlopen的类似。
urllib._urlopener：urlopen()和urlretrieve()返回FancyURLopener类的实例，可以创建URLopener类或FancyURLopener类的子类，然后把子类的实例赋给_urlopener。
urllib.urlcleanup()：清除由urlretrieve()产生的缓存。
urllib.quote(string[, safe])：把字符串里的特殊字符用%xx代替。字母、数字和下划线（_）总是不会被代替。safe参数指定不被替代的字符，默认是/。
urllib.quote_plus(string[, safe])：与quote()类似，同时空格也会用正号代替，而正号会用%xx代替。
urllib.unquote(string)：把%xx还原为特殊字符。
urllib.unquote_plus(string)：把%xx还原为特殊字符，包括空格。
urllib.urlencode(query[, doseq])：把两元素的元组转换为编码的字符串，如key=value，中间用&连接，可用于POST的请求。
urllib.pathname2url(path)：把路径从本地语法转换为URL。
urllib.url2pathname(path)：把路径的百分号编码的URL转成本地的语法。
urllib.getproxies()：返回代模式标识与理服务器URL的对应字典。
'''

'''
URLopener类：
class urllib.URLopener([proxies[, context[, **x509]]])：参数参考urlopen()。x509是另外的键值对，可用于https:的授权。
方法：
open(fullurl[, data])：参考urlopen()。
open_unknown(fullurl[, data])：打开未知的URL类型。
retrieve(url[, filename[, reporthook[, data]]])： 参考urlretrieve()。
version：对象的User Agent。

FancyURLopener类：
class urllib.FancyURLopener(...)：URLopener类的子类。
方法：
prompt_user_passwd(host, realm)：对于给定的指定区域的主机，返回用户验证信息，以(user,password)元组的形式。
'''

'''
异常
exception urllib.ContentTooShortError(msg[, content])：urlretrieve()函数检测到下载的数据少于期望的数据（通过Content-Length header指定），抛出此异常。
'''

def test_urllib():
    # 发起GET请求
    f = urllib.urlopen('http://www.baidu.com')
    print f.read()

    # GET请求，传于参数，来自官网
    params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})  # 参数字典
    print '*' * 200
    print params
    # GET
    f = urllib.urlopen('http://www.musi-cal.com/cgi-bin/query?%s' % params)
    print f.read()

    # POST请求，来自官网
    f = urllib.urlopen('http://www.musi-cal.com/cgi-bin/query', params)
    print '*' * 200
    print f.read()

    # 使用代理，来自官网，貌似不Work
    # proxies = {'http': 'http://proxy.example.com:8080/'}
    # opener = urllib.FancyURLopener(proxies)
    # f = opener.open('http://www.python.org')
    # print '*' * 200
    # print f.read()

    # 不用代理，来自官网
    opener = urllib.FancyURLopener({})
    f = opener.open('http://www.python.org/')
    print '*' * 200
    print f.read()

    # 下载到本地
    f = urllib.urlretrieve('http://www.baidu.com')
    print '*' * 200
    print f


if __name__ == '__main__':
    test_urllib()
