# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_id',
            field=models.CharField(max_length=20, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_token',
            field=models.CharField(max_length=1000, unique=True, null=True, blank=True),
        ),
    ]
