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
def duduru(inp, nick=''):
    '''.du/.duduru <sentense> -- talk to cleverbot http://www.cleverbot.com'''
    return 'cleverbot的验证方式貌似改了, 所以暂时用不了聊天功能了呢:(\n基佬们空虚寂寞的时候先去找smbot暂时解决吧:P'
    # if nick not in userlist:
        # out = "Duduru~ 真由しいです\n" + cbs.Ask(inp)
        # userlist.append(nick)
    # else:
    # out = cbs.Ask(inp)
    # return out

@hook.regex('^duduru')
def durep(msg, nick=''):
    out = cbs.Ask(msg)
    return out

# settings.configure()
# request = HttpRequest()
# request.POST['message'] = 'test'
# request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
