# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0009_auto_20160904_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='utested',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
