# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('office', '0001_initial'),
        ('phone', '0002_phone_contact_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='office',
            field=models.ForeignKey(default='433e9767-10da-4c1d-9b79-a64fecb783d2', to='office.Office'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='organization',
            field=models.ForeignKey(default='9399df6c-7263-40c0-bbdd-a3b07e031043', to='organization.Organization'),
            preserve_default=False,
        ),
    ]
