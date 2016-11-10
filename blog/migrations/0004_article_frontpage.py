# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='frontpage',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
