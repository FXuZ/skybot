#!/usr/bin/env python2
#-*-coding:utf-8-*-
import urllib2
import re
from util import hook


def get_torrent(key, order=5):
    # order 决定怎么排列：0 --- 相关度；1 --- 下载量；2 --- 添加时间；3 ---
    # 大小；4 --- 文件类型；5 --- 评分。
    url = 'http://btdigg.org/search?q=%s&p=0&order=%d'
    skey = urllib2.quote(key.decode('utf8').encode('utf8'))
    tmp = urllib2.urlopen(url % (skey, order))
    content = tmp.read().decode('utf8')
    tmp.close()
    return content


@hook.command('fuli')
def get_magnet(key):
    result = re.search('(?<="magnet)[^"]*(?=")', get_torrent(key))
    if result:
        result = "magnet" + result.group()
    else:
        result = "乃个变态到底想要啥种子？！"
        return result
