# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0002_auto_20150730_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='uid',
            field=models.CharField(db_index=True, max_length=255, verbose_name='uid'),
        ),
    ]
