# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_added_to_map',
            field=models.BooleanField(default=0),
        ),
    ]
