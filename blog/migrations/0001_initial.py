# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(default='Skriv tittel her', max_length=200)),
                ('description', models.CharField(default='Skriv beskrivelse her', max_length=500)),
                ('body', models.TextField(default='Skriv artikkelen her', max_length=4000)),
                ('author', models.CharField(default='Ditt navn', max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('publishDate', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
