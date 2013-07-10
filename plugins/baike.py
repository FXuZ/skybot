#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import re
from util import hook


def geturl(key):
    url = 'http://baike.baidu.com/search?word=%s&type=0&pn=0&rn=10&submit=search'
    # skey = urllib.quote(key.encode('gbk'))
    skey = key.encode('gbk').strip()
    req = urllib2.Request(url % skey)
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    tmp = opener.open(req)
    # tmp = urllib.urlopen(url % skey)
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
