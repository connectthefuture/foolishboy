# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooler', '0003_auto_20151019_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtime',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
