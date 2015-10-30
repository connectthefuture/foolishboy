# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooler', '0004_auto_20151019_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qanswer', models.CharField(max_length=1024)),
                ('qtitle', models.ForeignKey(to='fooler.question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
