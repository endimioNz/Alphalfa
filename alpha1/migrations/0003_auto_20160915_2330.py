# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha1', '0002_auto_20160915_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinario',
            name='acreditacion_aie',
            field=models.CharField(max_length=15, null=True, verbose_name='Numero de Acreditacion de A.I.E.'),
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='acreditacion_brucelosis',
            field=models.CharField(max_length=15, null=True, verbose_name='Numero de Acreditacion de Brucelosis'),
        ),
    ]