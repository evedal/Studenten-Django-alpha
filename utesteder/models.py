from django.db import models
from Studenten import settings
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class By(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']


class Utested(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    body = models.TextField(max_length=2000)
    description = models.CharField(max_length=150)
    apningstider = models.TextField(max_length=100, default="Mandag-fredag: 00:00-00:00 Lordag: 00:00-00:00 Sondag: 00:00-00:00")
    olpriser = models.TextField(max_length=100, default="Dahls fatol: 75kr,Rom og cola: 91kr")
    adresse = models.CharField(max_length=50,default="Bakkegata 26 7019 Trondheim")
    by = models.ForeignKey(By, default=0)
    image = models.ImageField(default=settings.MEDIA_ROOT)
    hScore = models.FloatField(default=0)
    aScore = models.FloatField(default=0)
    pScore = models.FloatField(default=0)
    dScore = models.FloatField(default=0)

    class Meta:
        ordering = ['name']

    def calcScore(self):
        hScore = 0
        aScore = 0
        pScore = 0
        dScore = 0
        aCount = 0
        pCount = 0
        dCount = 0
        anmeldelser = self.anmeldelse_set.all()
        for i in anmeldelser:
            if i.hScore != 0:
                hScore += i.hScore
            if i.aScore != 0:
                aScore += i.aScore
                aCount += 1
            if i.pScore != 0:
                pScore += i.pScore
                pCount += 1
            if i.dScore != 0:
                dScore += i.dScore
                dCount += 1


        self.hScore = hScore/len(anmeldelser)
        if aCount != 0:
            self.aScore = aScore/aCount
        else:
            self.aScore = 0
        if pCount != 0:
            self.pScore = pScore / pCount
        else:
            self.pScore = 0
        if dCount != 0:
            self.dScore = dScore / dCount
        else:
            self.dScore = 0
        self.save()



class Anmeldelse(models.Model):
    hScore = models.IntegerField(default=0)
    aScore = models.IntegerField(default=0)
    pScore = models.IntegerField(default=0)
    dScore = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000,default='Skriv en kommentar!')
    author = models.CharField(max_length=50,default='')
    date = models.DateField(default=timezone.datetime.now)
    utested = models.ForeignKey(Utested,default=0)
    review_rating = models.IntegerField(default=1)
    people_rated = models.ManyToManyField(User, through='Rating')

    class Meta:
        ordering = ['-review_rating']

    def save(self,*args,**kwargs):
        utesteder = Utested.objects.all()
        for u in utesteder:
            u.calcScore()
        super().save(*args, **kwargs)

#raiting can be [-1,0,1]
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Anmeldelse, on_delete=models.CASCADE)
    rated = models.IntegerField(default=0, max_length=1)