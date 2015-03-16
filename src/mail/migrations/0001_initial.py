# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, primary_key=True, default=uuid.uuid4)),
                ('created_on', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('deleted_on', models.DateTimeField(null=True, blank=True, verbose_name='Deleted on', default=None)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=200)),
                ('country', models.ForeignKey(to='country.Country')),
                ('organization', models.ForeignKey(to='organization.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
