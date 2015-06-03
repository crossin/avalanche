# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowball', '0002_stock_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
