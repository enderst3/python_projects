# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-05-14 04:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_prioritiy',
            new_name='task_priority',
        ),
    ]
