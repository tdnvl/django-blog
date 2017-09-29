# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Recommended Link',
                'verbose_name_plural': 'Recommended Links',
            },
        ),
        migrations.CreateModel(
            name='SiteLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Site Link',
                'verbose_name_plural': 'Site Links',
            },
        ),
    ]