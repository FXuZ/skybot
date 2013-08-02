'''Searches wikipedia and returns first sentence of article
Scaevolus 2009'''

import re

from util import hook, http
# from lxml import etree


api_prefix = "https://wiki.archlinux.org/api.php"
search_url = api_prefix + "?format=json&action=opensearch&namespace=0&suggest="
index_prefix = "https://wiki.archlinux.org/index.php"

paren_re = re.compile('\s*\(.*\)$')


@hook.command('aw')
@hook.command
def archwiki(inp):
    '''.aw/.archwiki <phrase> -- gets first sentence of archwiki ''' \
    '''article on <phrase>'''

    x = http.get_json(search_url, search=inp)
    sug = x[1]
    if len(sug) is 0:
        return "啊啦没找到这个主题呢~"
    else:
        key = sug[0]
        page = http.get(index_prefix, search=key, title='Special Search')
        print(key)
        result = re.search('(?=<p>).*%s.*[i\'\s][is].*\s<\/p>' % key,
                           page, re.IGNORECASE)
        result = strip_label(result)
        if len(result.group()) > 300:
            result = result.group()[:300]

        cnturl = (index_prefix + "/%s") % sug[0]
        # msg =  strip_label(result.group())+' -- '+cnturl
        msg = '%s -- %s' % (result, cnturl)
        return msg


def strip_label(html_str):
    return re.sub('<[^<>]*>', '', html_str).strip()
