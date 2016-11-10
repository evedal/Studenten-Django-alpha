# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0012_auto_20160907_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='anmeldelse',
            name='title',
            field=models.CharField(default='Title', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 7, 12, 3, 52, 440593, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
