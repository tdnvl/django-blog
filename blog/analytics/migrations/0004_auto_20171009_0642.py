# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20171009_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagerequest',
            name='ip_addr',
            field=models.CharField(max_length=255, verbose_name='IP Address of Request'),
        ),
        migrations.AlterField(
            model_name='pagerequest',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
