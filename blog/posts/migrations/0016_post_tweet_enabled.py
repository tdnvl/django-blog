# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-26 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20171020_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tweet_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
