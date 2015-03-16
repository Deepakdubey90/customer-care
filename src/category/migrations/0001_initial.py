# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('deleted_on', models.DateTimeField(verbose_name='Deleted on', default=None, null=True, blank=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
