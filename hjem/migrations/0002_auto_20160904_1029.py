# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hjem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bruker',
            name='tidOpprettet',
            field=models.TimeField(default=datetime.datetime(2016, 9, 4, 10, 29, 30, 521939)),
            preserve_default=True,
        ),
    ]
