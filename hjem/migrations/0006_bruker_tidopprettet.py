# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hjem', '0005_remove_bruker_tidopprettet'),
    ]

    operations = [
        migrations.AddField(
            model_name='bruker',
            name='tidOpprettet',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
