# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_image_image_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
