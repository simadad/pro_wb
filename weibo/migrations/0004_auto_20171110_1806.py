# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0003_auto_20171110_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='weibo.WeiBo', verbose_name='微博'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=500, verbose_name='评论'),
        ),
    ]
