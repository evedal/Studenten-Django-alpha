# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utested',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=1000)),
                ('apningstider', models.TextField(max_length=100)),
                ('olpriser', models.TextField(max_length=100)),
                ('adresse', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
