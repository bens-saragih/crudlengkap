# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-21 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosmed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='context',
            field=models.CharField(default='tes', max_length=100),
            preserve_default=False,
        ),
    ]