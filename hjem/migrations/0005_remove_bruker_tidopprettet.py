# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hjem', '0004_bruker_tidopprettet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bruker',
            name='tidOpprettet',
        ),
    ]
