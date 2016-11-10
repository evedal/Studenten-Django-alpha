# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160925_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 7, 14, 1, 48, 186664, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
