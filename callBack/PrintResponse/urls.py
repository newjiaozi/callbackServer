#coding:utf-8
'''
Created on 2016��10��28��

@author: ldl
'''
from django.conf.urls import url
from .views import callback


urlpatterns = [
    url(r'^', callback),
]