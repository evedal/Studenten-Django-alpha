# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20161018_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 20, 7, 37, 54, 545602, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
