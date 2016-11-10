from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$', 'utesteder.views.index', name='index'),
    url(r'^([0-9]{1,4})/$', 'utesteder.views.utested', name='utesteder'),
    url(r'^(?P<id>[0-9]{1,4})/(?P<review_amount>\d{0,50})/$', 'utesteder.views.utested', name='utesteder'),
    url(r'^upvote/([0-9]{1,4})/$', 'utesteder.views.upvote', name='upvote'),
    url(r'^downvote/([0-9]{1,4})/$', 'utesteder.views.downvote', name='downvote'),

    #url(r'^([0-9]{1})/review/$', 'utesteder.views.utested', name='utested'),

]