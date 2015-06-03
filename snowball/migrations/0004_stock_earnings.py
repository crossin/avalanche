# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowball', '0003_stock_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='earnings',
            field=models.FloatField(default=0),
        ),
    ]
