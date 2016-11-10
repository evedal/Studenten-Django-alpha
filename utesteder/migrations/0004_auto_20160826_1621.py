# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0003_anmeldelse'),
    ]

    operations = [
        migrations.AddField(
            model_name='anmeldelse',
            name='aScore',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='comment',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='dScore',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='hScore',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='pScore',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
