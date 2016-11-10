from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([0-9]{1,4})/$', 'blog.views.index', name='index'),
    url(r'^article/([0-9]{1,4})/$', 'blog.views.article', name='article'),
    url(r'^pagecount/([0-9]{1,4})/$', 'blog.views.page_count', name='page_count'),

]