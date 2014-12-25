# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_thread_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='image_link',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
