# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='population',
            field=models.IntegerField(blank=True),
        ),
    ]
