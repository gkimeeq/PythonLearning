#!/usr/bin/env python
# coding=utf-8

import urllib2

'''
urllib2可以简单认为是urllib的增强版，但由于urllib中提供了urllib2中没有的函数，因为又不能完全替代urllib。
两者不能相互替代 ，只能是配合着使用。urllib和urllib2的区别：
urllib2通过Request参数来修改Header，也就是可以通过更改User Agent来伪装浏览器。
urllib提供urlencode函数，支持编码，如果在模拟登陆时，当需要编码之后的参数，就只能用urllib。
urllib提供了一系列如urlretrieve，quote等函数，而在urllib2中并没有。
'''

'''
urllib2模块：https://docs.python.org/2/library/urllib2.html

urllib2.urlopen(url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]])
urllib2.install_opener(opener)
urllib2.build_opener([handler, ...])
exception urllib2.URLError
exception urllib2.HTTPError

Request类：
class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
Request.add_data(data)
Request.get_method()
Request.has_data()
Request.get_data()
Request.add_header(key, val)
Request.add_unredirected_header(key, header)
Request.has_header(header)
Request.get_full_url()
Request.get_type()
Request.get_host()
Request.get_selector()
Request.get_header(header_name, default=None)
Request.header_items()
Request.set_proxy(host, type)
Request.get_origin_req_host()
Request.is_unverifiable()

OpenerDirector类：
class urllib2.OpenerDirector
OpenerDirector.add_handler(handler)
OpenerDirector.open(url[, data][, timeout])
OpenerDirector.error(proto[, arg[, ...]])

BaseHandler类：
class urllib2.BaseHandler
BaseHandler.add_parent(director)
BaseHandler.close()
BaseHandler.parent
BaseHandler.default_open(req)
BaseHandler.protocol_open(req)
BaseHandler.unknown_open(req)
BaseHandler.http_error_default(req, fp, code, msg, hdrs)
BaseHandler.http_error_nnn(req, fp, code, msg, hdrs)
BaseHandler.protocol_request(req)
BaseHandler.protocol_response(req, response)

HTTPDefaultErrorHandler类：
class urllib2.HTTPDefaultErrorHandler

HTTPRedirectHandler类：
class urllib2.HTTPRedirectHandler
HTTPRedirectHandler.redirect_request(req, fp, code, msg, hdrs, newurl)
HTTPRedirectHandler.http_error_301(req, fp, code, msg, hdrs)
HTTPRedirectHandler.http_error_302(req, fp, code, msg, hdrs)
HTTPRedirectHandler.http_error_303(req, fp, code, msg, hdrs)
HTTPRedirectHandler.http_error_307(req, fp, code, msg, hdrs)

HTTPCookieProcessor类：
class urllib2.HTTPCookieProcessor([cookiejar])
HTTPCookieProcessor.cookiejar

ProxyHandler类：
class urllib2.ProxyHandler([proxies])
ProxyHandler.protocol_open(request)

HTTPPasswordMgr类：
class urllib2.HTTPPasswordMgr
HTTPPasswordMgr.add_password(realm, uri, user, passwd)
HTTPPasswordMgr.find_user_password(realm, authuri)

HTTPPasswordMgrWithDefaultRealm类：
class urllib2.HTTPPasswordMgrWithDefaultRealm

AbstractBasicAuthHandler类：
class urllib2.AbstractBasicAuthHandler([password_mgr])
AbstractBasicAuthHandler.http_error_auth_reqed(authreq, host, req, headers)

HTTPBasicAuthHandler类：
class urllib2.HTTPBasicAuthHandler([password_mgr])
HTTPBasicAuthHandler.http_error_401(req, fp, code, msg, hdrs)

ProxyBasicAuthHandler类：
class urllib2.ProxyBasicAuthHandler([password_mgr])
ProxyBasicAuthHandler.http_error_407(req, fp, code, msg, hdrs)

AbstractDigestAuthHandler类：
class urllib2.AbstractDigestAuthHandler([password_mgr])
AbstractDigestAuthHandler.http_error_auth_reqed(authreq, host, req, headers)

HTTPDigestAuthHandler类：
class urllib2.HTTPDigestAuthHandler([password_mgr])
HTTPDigestAuthHandler.http_error_401(req, fp, code, msg, hdrs)

ProxyDigestAuthHandler类：
class urllib2.ProxyDigestAuthHandler([password_mgr])
ProxyDigestAuthHandler.http_error_407(req, fp, code, msg, hdrs)

HTTPHandler类：
class urllib2.HTTPHandler
HTTPHandler.http_open(req)

HTTPSHandler类：
class urllib2.HTTPSHandler([debuglevel[, context]])
HTTPSHandler.https_open(req)

FileHandler类：
class urllib2.FileHandler
FileHandler.file_open(req)

FTPHandler类：
class urllib2.FTPHandler
FTPHandler.ftp_open(req)

CacheFTPHandler类：
class urllib2.CacheFTPHandler
CacheFTPHandler.setTimeout(t)
CacheFTPHandler.setMaxConns(m)

UnknownHandler类：
class urllib2.UnknownHandler
UnknownHandler.unknown_open()

HTTPErrorProcessor类：
class urllib2.HTTPErrorProcessor
HTTPErrorProcessor.http_response()
HTTPErrorProcessor.https_response()
'''


def test_urllib2():
    # 获取页面，显示前100个字节
    f = urllib2.urlopen('https://www.baidu.com')
    print f.read(100)

    # 设置请求头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    # 创建Request对象，传入请求头
    req = urllib2.Request(url='https://www.baidu.com', headers=headers)
    # 传入Request对象来接收页面
    resp = urllib2.urlopen(req)
    # 读取页面文本
    html = resp.read()
    print '*' * 200
    print html
    print '*' * 200
    print resp.getcode()  # 响应码
    print resp.geturl()  # url
    print resp.info()  # 报头


if __name__ == '__main__':
    test_urllib2()
