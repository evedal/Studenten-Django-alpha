# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20160904_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField(default=datetime.datetime(2016, 9, 17, 15, 6, 24, 534679, tzinfo=utc))),
                ('body', models.TextField(max_length=1000)),
                ('article', models.ForeignKey(to='blog.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
    ]
