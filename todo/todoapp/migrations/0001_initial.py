# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-05-13 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_prioritiy', models.CharField(max_length=200)),
            ],
        ),
    ]
