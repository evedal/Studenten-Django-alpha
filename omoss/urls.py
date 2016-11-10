from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'omoss.views.index', name='index'),
]