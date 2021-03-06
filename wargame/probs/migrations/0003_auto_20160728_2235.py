# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probs', '0002_problem_prob_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='prob_category',
            field=models.CharField(choices=[(b'PWN', b'pwnable'), (b'REV', b'reversing'), (b'WEB', b'web'), (b'FRS', b'forensic'), (b'CRT', b'crypto')], default=b'PWN', max_length=3),
        ),
    ]
