# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
