from django.db import models
from django.utils import timezone
from Studenten import settings
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Article(models.Model):
    DEFAULT_AUTHOR = 1
    title = models.CharField(max_length=200,default="Skriv tittel her")
    description = models.CharField(max_length=500,default="Skriv beskrivelse her")
    body = models.TextField(max_length=4000,default="Skriv artikkelen her")
    author = models.ForeignKey(User, default=DEFAULT_AUTHOR)
    image = models.ImageField(null=True,default=settings.MEDIA_ROOT)
    publishDate = models.DateTimeField(timezone.now)
    frontpage = models.BooleanField(default=False)
    tags = TaggableManager()
    hit_count = models.IntegerField(default=0)

class ArticleComment(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now())
    body = models.TextField(max_length=1000)
    article = models.ForeignKey(Article)


