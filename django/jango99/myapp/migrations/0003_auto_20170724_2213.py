# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170724_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=400),
        ),
    ]
