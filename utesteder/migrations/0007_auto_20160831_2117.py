# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0006_auto_20160826_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anmeldelse',
            name='aScore',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='comment',
            field=models.TextField(default='', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='dScore',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='pScore',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utested',
            name='image',
            field=models.ImageField(upload_to='/media/'),
            preserve_default=True,
        ),
    ]
