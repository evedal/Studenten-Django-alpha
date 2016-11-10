'''
Created on 22. okt. 2015

@author: Evdal
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'hjem.views.index', name='index'),
]