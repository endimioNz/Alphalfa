# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 23:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha1', '0004_auto_20160915_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametros',
            name='isBoolean',
        ),
        migrations.RemoveField(
            model_name='parametros',
            name='isFloat',
        ),
        migrations.RemoveField(
            model_name='parametros',
            name='isInteger',
        ),
        migrations.RemoveField(
            model_name='parametros',
            name='isString',
        ),
    ]