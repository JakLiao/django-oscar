# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-13 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20170413_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
    ]
