# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_items_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='img_loc',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
