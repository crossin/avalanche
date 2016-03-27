# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowball', '0005_auto_20150604_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='KLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('price_open', models.FloatField(default=0)),
                ('price_close', models.FloatField(default=0)),
                ('price_max', models.FloatField(default=0)),
                ('price_min', models.FloatField(default=0)),
                ('volume', models.IntegerField(default=0)),
                ('turnover', models.IntegerField(default=0)),
                ('stock', models.ForeignKey(related_name='kline', to='snowball.Stock')),
            ],
        ),
    ]
