# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinario',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]