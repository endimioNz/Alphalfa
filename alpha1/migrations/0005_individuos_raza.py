# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 23:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpha1', '0004_auto_20161103_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='individuos',
            name='raza',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='alpha1.Raza'),
            preserve_default=False,
        ),
    ]
