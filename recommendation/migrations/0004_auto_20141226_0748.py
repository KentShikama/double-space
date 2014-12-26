# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_auto_20141225_2029')
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='detail_link',
            field=models.TextField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='image_link',
            field=models.TextField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='poster',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
