from django.db import models
from utesteder import models as uModels
from django.utils import timezone
# Create your models here.

class Bruker(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    passord = models.CharField(max_length=50)
    fornavn = models.CharField(max_length=50)
    etternavn = models.CharField(max_length=50)
    by = models.ForeignKey(uModels.By)
    tidOpprettet = models.DateTimeField(default=timezone.now)
