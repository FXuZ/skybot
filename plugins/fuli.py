#!/usr/bin/env python2
#-*-coding:utf-8-*-
import urllib2
import re
from util import hook


def get_torrent(key, order=0):
    # order 决定怎么排列：0 --- 相关度；1 --- 下载量；2 --- 添加时间；3 ---
    # 大小；4 --- 文件类型；5 --- 评分。
    url = 'http://btdigg.org/search?q=%s&p=0&order=%d'
    skey = urllib2.quote(key.decode('utf8').encode('utf8'))
    tmp = urllib2.urlopen(url % (skey, order))
    content = tmp.read().decode('utf8')
    tmp.close()
    return content


@hook.command('fl')
@hook.command('fuli')
def get_magnet(key):
    '''.fl/.fuli <keywords> -- 从http://btdigg.org 上搜索福利并且返回评分最高的结果的磁力链.
    '''
    magnet_url = get_torrent(key)
    print magnet_url
    result = re.search('(?<="magnet)[^"]*(?=")', magnet_url)
    if result:
        result = "magnet" + result.group()
    else:
        result = "乃个变态到底想要啥种子？！"
    return result
