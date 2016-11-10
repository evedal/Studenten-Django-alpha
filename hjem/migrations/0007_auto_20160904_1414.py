# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hjem', '0006_bruker_tidopprettet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bruker',
            name='tidOpprettet',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
