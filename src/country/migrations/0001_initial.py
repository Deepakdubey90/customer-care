# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(verbose_name='Updated on', auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, verbose_name='Deleted on', null=True)),
                ('name', models.CharField(max_length=200)),
                ('code_2', models.CharField(null=True, max_length=2)),
                ('code_3', models.CharField(null=True, max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
