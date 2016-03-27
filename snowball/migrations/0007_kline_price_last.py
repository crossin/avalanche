# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowball', '0006_kline'),
    ]

    operations = [
        migrations.AddField(
            model_name='kline',
            name='price_last',
            field=models.FloatField(default=0),
        ),
    ]
