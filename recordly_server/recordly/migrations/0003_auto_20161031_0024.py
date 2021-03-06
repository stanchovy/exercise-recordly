# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-31 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recordly', '0002_auto_20161023_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='recordly.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('title', 'artist', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together=set([('name', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together=set([('title', 'album', 'user')]),
        ),
    ]
