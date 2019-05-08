# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 17:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('step', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='school',
            new_name='school_key',
        ),
        migrations.AddField(
            model_name='level',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='school_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='step.School'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]