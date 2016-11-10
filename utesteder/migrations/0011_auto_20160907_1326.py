# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0010_utested_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='by',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='utested',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='author',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='anmeldelse',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 7, 11, 25, 55, 283678, tzinfo=utc), default=datetime.datetime(2016, 9, 7, 11, 26, 16, 130109, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='comment',
            field=models.TextField(max_length=500, default='Skriv en kommentar!'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='anmeldelse',
            name='hScore',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utested',
            name='description',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
