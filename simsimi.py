from django.http import *
from django.conf import settings
import requests
import cookielib


def simsimi(request):
    if request.is_ajax():
        message = request.POST['message']
        chat_url = 'http://www.simsimi.com/func/req?lc=ch&msg=%s'
        # chat_url = 'http://xiaojiji.duapp.com/simsimi.php?key=%s'
        r = requests.get('http://www.simsimi.com/talk.htm')
        chat_cookies = r.cookies
        chat_headers = {
            'Referer': 'http://www.simsimi.com/talk.htm?lc=ch',
            'User-Agent': 'AgentMozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20130529 Firefox/21.0 FirePHP/0.7.2',
            'Host': 'www.simsimi.com',
            'x-insight': 'activate'
        }
        r = requests.get(chat_url % message,
                         cookies=chat_cookies, headers=chat_headers)
        if len(r.json()) == 0:
            return HttpResponse("hehe...")
        else:
            return HttpResponse(r.json()['response'])

import re
from util import hook, http


@hook.command('ss')
@hook.command
def simi(inp):
    '''.simi <sentense> -- talk to simsimi'''

    out = "Duduru~~ This is Mayushii~~\n" + simsimi(inp)
    return out


settings.configure()
request = HttpRequest()
request.POST['message'] = 'test'
request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
request.META['HTTP_USER_AGENT'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20130529 Firefox/21.0 FirePHP/0.7.2'
a = simsimi(request)
print a
