# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, default=uuid.uuid4, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('deleted_on', models.DateTimeField(default=None, null=True, verbose_name='Deleted on', blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('entity_object_id', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('entity_content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
