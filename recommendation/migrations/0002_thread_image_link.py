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
            name='image_link',
            field=models.TextField(default='http://img4.imgtn.bdimg.com/it/u=4198070164,3219625480&fm=21&gp=0.jpg'),
            preserve_default=True,
        ),
    ]
