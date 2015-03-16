# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('deleted_on', models.DateTimeField(default=None, null=True, blank=True, verbose_name='Deleted on')),
                ('name', models.CharField(max_length=200)),
                ('state', models.ForeignKey(to='state.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
