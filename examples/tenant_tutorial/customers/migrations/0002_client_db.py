# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-01-31 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='db',
            field=models.CharField(choices=[(b'default', b'default'), (b'db1', b'db1'), (b'db2', b'db2')], default=b'dafault', max_length=200, verbose_name=b'db_choices'),
        ),
    ]