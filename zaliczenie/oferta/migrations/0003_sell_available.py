# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0002_auto_20170123_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]