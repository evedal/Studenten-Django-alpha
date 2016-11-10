from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import urls as urls
from hjem import urls as urls2
from accounts import urls as urls4
from utesteder import urls as urls3
from django.conf.urls.static import static
from django.conf import settings
from omoss import urls as urls5
urlpatterns = [
    # Examples:
    url(r'^$', include(urls2)),
    url(r'hjem/', include(urls2)),
    url(r'blog/', include(urls)),
    url(r'utesteder/', include(urls3)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(urls4)),
    url(r'^omoss/', include(urls5)),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


