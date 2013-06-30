'''Searches wikipedia and returns first sentence of article
Scaevolus 2009'''

import re

from util import hook, http
from lxml import etree


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
        rslt = http.get_xml(index_prefix, search=sug[0],
                            title='Special Search')
        for e in rslt.iter('h1'):
            if 'id' in e.attrib and'firstHeading' == e.attrib['id']:
                hd = e
                break
        topic = strip_label(etree.tostring(hd))
        for e in rslt.iter('div'):
            attrs = e.attrib
            if 'id' in attrs and 'mw-content-text' == attrs['id']:
                cont = e
                break
        for e in cont.iter('p'):
            if topic in etree.tostring(e):
                first_para = e
                break
        # first_para = cont[3]
        cnturl = (index_prefix + "/%s") % sug[0]
        desc = strip_label(etree.tostring(first_para))
        if len(desc) > 300:
            desc = desc[:300] + '...'
        return '%s -- %s' % (desc, cnturl)


def strip_label(html_str):
    return re.sub('<[^<>]*>', '', html_str).strip()
