# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161007_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 12, 10, 49, 31, 817775, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
