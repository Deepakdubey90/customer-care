# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Deleted on')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='category.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
