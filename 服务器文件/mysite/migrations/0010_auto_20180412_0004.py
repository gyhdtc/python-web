# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20180412_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(default=b'', max_length=30),
        ),
    ]
