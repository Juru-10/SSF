# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0003_auto_20190510_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='comment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='marks',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]
