# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170403_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='headline',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
