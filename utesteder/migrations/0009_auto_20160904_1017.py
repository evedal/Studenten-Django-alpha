# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0008_auto_20160901_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utested',
            name='adresse',
            field=models.CharField(max_length=50, default='Bakkegata 26 7019 Trondheim'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utested',
            name='apningstider',
            field=models.TextField(max_length=100, default='Mandag-fredag: 00:00-00:00 Lørdag: 00:00-00:00 Søndag: 00:00-00:00'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utested',
            name='image',
            field=models.ImageField(upload_to='', default='C:/Users/Evdal/Documents/Studenten-Django/media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utested',
            name='olpriser',
            field=models.TextField(max_length=100, default='Dahls fatøl: 75kr,Rom og cola: 91kr'),
            preserve_default=True,
        ),
    ]
