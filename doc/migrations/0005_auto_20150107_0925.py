# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0004_auto_20150107_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=128, unique=True, null=True),
            preserve_default=True,
        ),
    ]
