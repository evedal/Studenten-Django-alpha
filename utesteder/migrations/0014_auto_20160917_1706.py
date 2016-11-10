# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0013_auto_20160907_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anmeldelse',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
