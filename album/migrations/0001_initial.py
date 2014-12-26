# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
