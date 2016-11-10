# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0005_auto_20160826_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anmeldelse',
            name='utested',
            field=models.ForeignKey(to='utesteder.Utested', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utested',
            name='by',
            field=models.ForeignKey(to='utesteder.By', default=0),
            preserve_default=True,
        ),
    ]
