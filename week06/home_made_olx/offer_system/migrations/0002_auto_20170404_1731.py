# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='desription',
            new_name='description',
        ),
    ]