# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=120, null=True)),
                ('cena', models.DateTimeField(auto_now_add=True)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
