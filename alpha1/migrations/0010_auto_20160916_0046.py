# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha1', '0009_auto_20160916_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individuos',
            name='caravana',
        ),
        migrations.AddField(
            model_name='individuos',
            name='identificacion',
            field=models.CharField(default='1', max_length=10, verbose_name='Identificacion / N° de Caravana'),
            preserve_default=False,
        ),
    ]