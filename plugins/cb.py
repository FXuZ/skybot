# from django.http import *
# from django.conf import settings
# import requests
# import cookielib


import re
from util import hook, http
from util import cleverbot


userlist = []
cbs = cleverbot.Session()
@hook.command('du')
@hook.command
def duduru(inp, nick):
    '''.simi <sentense> -- talk to simsimi'''
    if nick not in userlist:
        out = "Duduru~~ This is Mayushii~~\n" + cbs.Ask(inp)
        userlist.append(nick)
    else:
        out = cbs.Ask(inp)
    return out


settings.configure()
request = HttpRequest()
request.POST['message'] = 'test'
request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'

