# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_delete_oferta'),
    ]

    operations = [
        migrations.CreateModel(
            name='oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=120, null=True)),
                ('cena', models.CharField(max_length=20, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]