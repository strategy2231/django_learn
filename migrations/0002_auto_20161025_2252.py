# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
        ),
    ]
