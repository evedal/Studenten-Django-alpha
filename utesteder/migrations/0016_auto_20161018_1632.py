# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('utesteder', '0015_auto_20161012_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anmeldelse',
            name='title',
        ),

    ]
