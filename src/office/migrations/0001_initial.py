# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('deleted_on', models.DateTimeField(blank=True, null=True, default=None, verbose_name='Deleted on')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('line1', models.CharField(max_length=200)),
                ('line2', models.CharField(blank=True, max_length=200, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.ForeignKey(to='city.City')),
                ('organization', models.ForeignKey(to='organization.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
