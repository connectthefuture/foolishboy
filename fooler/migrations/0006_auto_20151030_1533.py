# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooler', '0005_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
