# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_frontpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='C:/Users/Evdal/Documents/Studenten-Django/media', null=True, upload_to=''),
            preserve_default=True,
        ),
    ]
