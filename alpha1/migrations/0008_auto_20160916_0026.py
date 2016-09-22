# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha1', '0007_auto_20160916_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuos',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Macho'), ('H', 'Hembra'), ('X', 'NS/NC')], default='NS/NC', max_length=1, null=True, verbose_name='Sexo'),
        ),
    ]