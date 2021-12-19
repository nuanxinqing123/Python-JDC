# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 10:28
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : cookie.py

from qinglong import addCookie


# Cookie提取
def clear(ck):
    pt_pin, pt_key = None, None
    for i in ck:
        if i['name'] == 'pt_pin':
            pt_pin = i["value"]

        if i['name'] == 'pt_key':
            pt_key = i['value']

    ck = merge(key=pt_key, pin=pt_pin)
    return ck


# Cookie合并
def merge(key, pin):
    cookie = "pt_key={}; pt_pin={};".format(key, pin)
    print("已获取Cookie：" + cookie)
    return cookie
