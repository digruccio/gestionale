# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-19 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0003_auto_20191119_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fattura',
            name='Prodotto',
        ),
        migrations.AddField(
            model_name='fattura',
            name='Prodotto',
            field=models.ManyToManyField(null=True, to='gestionale.Prodotto'),
        ),
    ]
