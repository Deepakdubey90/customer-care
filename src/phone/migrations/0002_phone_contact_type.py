# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='contact_type',
            field=models.CharField(default='dfd', max_length=20),
            preserve_default=False,
        ),
    ]
