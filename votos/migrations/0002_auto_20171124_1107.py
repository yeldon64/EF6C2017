# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votos',
            name='voto',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='votos.Candidato'),
        ),
    ]
