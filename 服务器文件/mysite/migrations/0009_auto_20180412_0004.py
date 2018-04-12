# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20180411_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
