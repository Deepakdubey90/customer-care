# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, primary_key=True, default=uuid.uuid4)),
                ('created_on', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(verbose_name='Updated on', auto_now=True)),
                ('deleted_on', models.DateTimeField(default=None, verbose_name='Deleted on', blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(to='country.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
