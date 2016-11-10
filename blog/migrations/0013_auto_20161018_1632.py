# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161012_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 18, 14, 32, 2, 182346, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
