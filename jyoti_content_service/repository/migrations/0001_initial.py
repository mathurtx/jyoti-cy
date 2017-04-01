# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationFactTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('report_type', models.CharField(max_length=30)),
                ('report_type_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReportCountFactTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('report_count', models.ImageField(default=0, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ReportTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('report_type', models.CharField(max_length=30)),
                ('report_content', models.CharField(max_length=300)),
                ('evidence', models.CharField(blank=True, max_length=100)),
                ('data_source', models.CharField(max_length=2)),
                ('city', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]