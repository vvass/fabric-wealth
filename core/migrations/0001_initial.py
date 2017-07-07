# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('inventory_number', models.IntegerField(default=0)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Size')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='widgets',
            field=models.ManyToManyField(to='core.Widget'),
        ),
    ]
