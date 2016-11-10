# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utesteder', '0014_auto_20160917_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rated', models.IntegerField(default=0, max_length=1)),
                ('review', models.ForeignKey(to='utesteder.Anmeldelse')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='anmeldelse',
            options={'ordering': ['-review_rating']},
        ),
        migrations.RenameField(
            model_name='anmeldelse',
            old_name='rating',
            new_name='review_rating',
        ),
    ]
