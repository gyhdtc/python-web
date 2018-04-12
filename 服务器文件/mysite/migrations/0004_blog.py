# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20180311_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=30)),
                ('body', models.TextField(max_length=5000)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
