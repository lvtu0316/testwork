# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-11-14 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_biz_id', models.IntegerField(blank=True, null=True, verbose_name='业务id')),
                ('ip', models.CharField(max_length=30, verbose_name='ip')),
                ('alarm_type', models.CharField(max_length=50, verbose_name='报警类型')),
                ('source_time', models.DateTimeField(verbose_name='报警时间')),
            ],
        ),
    ]
