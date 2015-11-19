# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gadget_Survey',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('currentMobile', models.CharField(max_length=100)),
                ('current_Laptop_Pc', models.CharField(max_length=100)),
                ('likes_device', models.IntegerField(default=-1)),
                ('likes_device_description', models.TextField()),
                ('future_device', models.IntegerField(default=-1)),
                ('future_device_description', models.TextField()),
            ],
        ),
    ]
