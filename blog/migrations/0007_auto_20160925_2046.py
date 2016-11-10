# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160917_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hit_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 9, 25, 18, 46, 38, 443979, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
