# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_auto_20160815_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.Order', verbose_name='заказ'),
        ),
    ]
