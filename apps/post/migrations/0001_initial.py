# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0, verbose_name='关联')),
                ('title', models.CharField(help_text='标题', max_length=128, verbose_name='标题')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='日期', verbose_name='日期')),
                ('content', models.TextField(help_text='正文', verbose_name='正文')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField(default=0, verbose_name='关联')),
                ('name', models.CharField(max_length=128, verbose_name='名字')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='日期')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
            },
        ),
    ]