# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20180411_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
