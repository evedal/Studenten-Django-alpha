# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0009_auto_20160904_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bruker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=100)),
                ('passord', models.CharField(max_length=50)),
                ('fornavn', models.CharField(max_length=50)),
                ('etternavn', models.CharField(max_length=50)),
                ('tidOpprettet', models.TimeField(default=datetime.datetime(2016, 9, 4, 10, 17, 57, 210389))),
                ('by', models.ForeignKey(to='utesteder.By')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
