import re
# from util import hook, http

import cookielib
import urllib
import urllib2
# import lxml


cookies = cookielib.CookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
]
opener = urllib2.build_opener(*handlers)


def open_get(uri):
    req = urllib2.Request(uri)
    return opener.open(req)


def open_post(url, post_data):
    req = urllib2.Request(url, urllib.urlencode(post_data))
    req.get_method = lambda: 'POST'
    print req.get_method()
    response = opener.open(req)
    return response


quest_url = 'http://www.pandorabots.com/pandora/talk?botid=c9c4b9bf6e345c25'


sessionid = ''
response = open_get(quest_url)
for cookie in cookies:
    if cookie.name == 'botcust2':
        sessionid = cookie.value
        print sessionid
        print response.read()


def Ask(message):
    post_data = {}
    post_data['message'] = message
    post_data['botcust2'] = sessionid
    response = open_post(quest_url, post_data)
    print response
    page = response.read()
    return page


def main():
    import sys
    q = ''
    while q != 'bye':
        try:
            q = raw_input('> ')
        except KeyboardInterrupt:
            print
            sys.exit()
        print Ask(q)

if __name__ == '__main__':
    main()
