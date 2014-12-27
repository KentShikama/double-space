# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='video_link',
            field=models.TextField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
    ]
