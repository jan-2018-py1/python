# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
