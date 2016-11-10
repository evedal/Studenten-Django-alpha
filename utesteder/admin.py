from django.contrib import admin

from .models import *
from blog.models import Article
admin.site.register(Utested)
admin.site.register(Anmeldelse)
admin.site.register(By)
admin.site.register(Article)


# Register your models here.
