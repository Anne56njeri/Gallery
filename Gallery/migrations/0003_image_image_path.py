# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0002_auto_20180504_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_path',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
