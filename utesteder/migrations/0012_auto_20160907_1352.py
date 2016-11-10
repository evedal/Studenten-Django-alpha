# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utesteder', '0011_auto_20160907_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anmeldelse',
            options={'ordering': ['-rating']},
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='people_rated',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 7, 11, 52, 57, 226114, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
