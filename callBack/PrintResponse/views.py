# from django.shortcuts import render
#coding:utf-8

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
import time


@csrf_exempt
def callback(request): 
    if request.method == "POST":
        print "[%s]====%s]" %(time.asctime(),request.body.decode('utf-8').encode("GBK"))
#         print request.body.decode('utf-8').encode("GBK")  
        
        
        return HttpResponse("RECEIVED")
    else:
        print "[%s]====%s" % (time.asctime(),"Not Post Request")
        return HttpResponse("Not Post Request")

  


