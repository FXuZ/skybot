#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import re
from util import hook


def geturl(key):
    url = 'http://baike.baidu.com/search?word=%s&type=0&pn=0&rn=10&submit=search'
    # skey = urllib.quote(key.encode('gbk'))
    skey = urllib2.quote(key.encode('gbk').strip())
    req = urllib2.Request(url % skey)
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    tmp = opener.open(req)
    # tmp = urllib.urlopen(url % skey)
    data = tmp.read().decode('gbk')
    tmp.close()
    return data


@hook.command('bk')
@hook.command('baike')
def re_get(key):
    ''' .bk/.baike <keywords> -- 返回百度百科第一个关于<keywords>的结果.
    '''
    tmp = geturl(key)
    text = re.search('\/view\/.*\.htm[l]?', tmp)
    if not text:
        return "百度百科弱爆了，没结果的说，乃快去创建吧！ ---- http://baike.baidu.com/create/%s&enc=gbk" % (urllib2.quote(key.decode('utf8').encode('gbk')))
    text = text.group()
    abstmp = re.search('(?<=<div class="abstract">\s{2}).*(?=<\/div>)',
                       tmp).group()
    abst = ""
    if abstmp:
        abst = " ---- " + re.sub("<[\/\w]*>", "", abstmp)
        msg = "http://baike.baidu.com" + text + abst
        return msg
