#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib.request
import urllib.parse
import re
from util import hook


def geturl(key):
    url = 'http://baike.baidu.com/search?word=%s&type=0&pn=0&rn=10&submit=search'
    skey = urllib.parse.quote(key.encode('gbk'))
    tmp = urllib.request.urlopen(url % skey)
    data = tmp.read().decode('gbk')
    tmp.close()
    return data


@hook.command('baike')
def re_get(key):
    text = re.search('\/view\/.*\.htm', geturl(key))
    if not text :
        return "没有找到结果！"
    text = text.group()
    msg = "http://baike.baidu.com" + text
    return msg
