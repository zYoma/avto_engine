# from django.shortcuts import render
from table.models import AuntificationLog
from table.models import get_client_ip
from django.contrib.auth.models import Group
from urllib.parse import unquote
# from django.urls import reverse
# from share.ban_date import check_ban_date

def write_log(func):
    
    def added_value(request, *args, **kwargs):
        if request.user.is_authenticated:
            l = request.user.groups.first().name
            if l != 'user':
                user = request.user
                ip = get_client_ip(request)
                useragent = request.META['HTTP_USER_AGENT']
                action = unquote(request.build_absolute_uri())
                new_log = AuntificationLog.objects.create(user = user, useragent=useragent, ip=ip, action=action)
       
        return func(request, *args, **kwargs)
          
            
    return added_value