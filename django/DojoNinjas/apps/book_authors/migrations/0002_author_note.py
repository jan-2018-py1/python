# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.TextField(default='none', max_length=600),
            preserve_default=False,
        ),
    ]