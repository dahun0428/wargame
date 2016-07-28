# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='prob_category',
            field=models.CharField(choices=[(b'PWN', b'Pwnable'), (b'REV', b'Reversing')], default=b'PWN', max_length=3),
        ),
    ]