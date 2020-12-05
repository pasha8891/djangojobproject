from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1>Hello Guest very'
    if h<12:
        msg=msg+'Good morning'
    elif h<16:
        msg=msg+'Good afternoon'
    elif h<21:
        msg=msg+'Good Evening'
    else:
        msg=msg+'Good night'
    msg=msg+'<h1>Now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
