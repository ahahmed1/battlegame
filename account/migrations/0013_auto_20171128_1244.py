# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20171128_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='belongings',
            name='acedemy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='belongings',
            name='museum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='belongings',
            name='warehouse',
            field=models.IntegerField(default=0),
        ),
    ]
