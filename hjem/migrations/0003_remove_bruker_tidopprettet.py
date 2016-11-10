# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hjem', '0002_auto_20160904_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bruker',
            name='tidOpprettet',
        ),
    ]
