# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0016_auto_20161018_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anmeldelse',
            name='comment',
            field=models.TextField(default='Skriv en kommentar!', max_length=1000),
            preserve_default=True,
        ),

        migrations.AlterField(
            model_name='utested',
            name='body',
            field=models.TextField(max_length=2000),
            preserve_default=True,
        ),
    ]
