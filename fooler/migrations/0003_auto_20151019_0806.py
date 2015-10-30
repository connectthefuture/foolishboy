# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooler', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtime',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
