from django import *
import requests
import cookielib


def simsimi(request):
    if request.is_ajax():
        message = request.POST.get('message')
        chat_url = 'http://www.simsimi.com/func/req?lc=ch&msg=%s'
        r = requests.get('http://www.simsimi.com/talk.htm')
        chat_cookies = r.cookies
        chat_headers = {
            'Referer': 'http://www.simsimi.com/talk.htm'
        }
        r = requests.get(chat_url % message,
                         cookies=chat_cookies, headers=chat_headers)
        if len(r.json()) == 0:
            return HttpResponse("hehe...")
        else:
            return HttpResponse(r.json()['response'])

import re
from util import hook, http


<<<<<<< HEAD
=======
@hook.command('ss')
>>>>>>> 131698230a1e05ec36b2dbbed9e918c0cc3e6f24
@hook.command
def simi(inp):
    '''.simi <sentense> -- talk to simsimi'''

<<<<<<< HEAD
=======
    out = "Duduru~~ This is Mayushii~~\n" + simsimi(inp)
>>>>>>> 131698230a1e05ec36b2dbbed9e918c0cc3e6f24
    return out
