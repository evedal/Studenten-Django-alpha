# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161007_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 7, 15, 4, 28, 400619, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
