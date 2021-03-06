# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-13 17:57
from __future__ import unicode_literals

from django.db import migrations

from oscar.core.compat import get_user_model

User = get_user_model()


def forwards_func(apps, schema_editor):
    for user in User.objects.all():
        user.emails.update(email=user.email)


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20170413_1853'),
    ]

    operations = [
        migrations.RunPython(forwards_func)
    ]
