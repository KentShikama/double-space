# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='app',
            field=models.CharField(max_length=128, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 19, 0, 20, 49794)),
            preserve_default=True,
        ),
    ]
