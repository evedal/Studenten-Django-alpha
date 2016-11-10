from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'accounts.views.login', name='login'),
    url(r'^auth/$', 'accounts.views.auth_view', name='auth'),
    url(r'^register/$', 'accounts.views.register', name='register'),
    url(r'^success/$', 'accounts.views.success', name='success'),
    url(r'^password/reset/$', 'accounts.views.forgot', name='password_reset'),
    url(r'^password/done/$', 'accounts.views.emailsent', name='password_reset_done'),
    url(r'^profile/$', 'accounts.views.profile', name='profile'),
    url(r'^profile/logout/$', 'accounts.views.logout', name='logout'),
    url(r'^profile/firstname/$', 'accounts.views.edit_firstname', name='edit_firstname'),
    url(r'^profile/lastname/$', 'accounts.views.edit_lastname', name='edit_lastname'),
    url(r'^profile/email/$', 'accounts.views.edit_email', name='edit_email'),
    url(r'^profile/password/$', 'accounts.views.edit_password', name='edit_password'),
]