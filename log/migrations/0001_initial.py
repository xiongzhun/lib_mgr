# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-07 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fibermotor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True, verbose_name='\u6807\u9898')),
                ('person', models.CharField(max_length=40, null=True, verbose_name='\u8d23\u4efb\u4eba')),
                ('start_time', models.DateField(verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('update_time', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('detail', models.CharField(max_length=40, null=True, verbose_name='\u5185\u5bb9')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fibermotor.Region', verbose_name='\u673a\u623f')),
            ],
            options={
                'verbose_name': '\u65e5\u5fd7\u5185\u5bb9',
                'verbose_name_plural': '\u65e5\u5fd7\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='Log_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, null=True, verbose_name='\u65e5\u5fd7\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u65e5\u5fd7\u7c7b\u578b',
                'verbose_name_plural': '\u65e5\u5fd7\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='log',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='log.Log_type', verbose_name='\u65e5\u5fd7\u7c7b\u578b'),
        ),
    ]