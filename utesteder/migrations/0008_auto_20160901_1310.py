# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0007_auto_20160831_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='utested',
            name='aScore',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='utested',
            name='dScore',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='utested',
            name='hScore',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='utested',
            name='pScore',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
