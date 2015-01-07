# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_auto_20150107_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
    ]
