# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-25 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20190324_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infographiccontent',
            options={'ordering': ('-infographic__pub_date', '-title')},
        ),
        migrations.AlterField(
            model_name='infographic',
            name='title',
            field=models.CharField(max_length=140, unique=True, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='infographiccontent',
            name='title',
            field=models.CharField(max_length=140, unique=True, verbose_name='Title'),
        ),
    ]
