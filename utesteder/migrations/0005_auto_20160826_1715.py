# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0004_auto_20160826_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='By',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='utested',
            field=models.ForeignKey(to='utesteder.Utested', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utested',
            name='by',
            field=models.ForeignKey(to='utesteder.By', default=1),
            preserve_default=False,
        ),
    ]
