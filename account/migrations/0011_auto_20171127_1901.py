# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20171127_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='photo',
            new_name='avatar',
        ),
    ]
