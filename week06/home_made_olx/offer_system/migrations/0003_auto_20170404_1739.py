# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_system', '0002_auto_20170404_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
