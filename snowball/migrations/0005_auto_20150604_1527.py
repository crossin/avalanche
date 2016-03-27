# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowball', '0004_stock_earnings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('weight_in', models.FloatField(default=0)),
                ('weight_out', models.FloatField(default=0)),
                ('earnings', models.FloatField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='earnings',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='weight_in',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='weight_out',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='stock',
            field=models.ForeignKey(related_name='logs', to='snowball.Stock'),
        ),
    ]
