# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-22 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20181022_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
    ]
