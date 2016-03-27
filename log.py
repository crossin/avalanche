import urllib2
import json
import time
import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='avalanche.settings'
django.setup()

from snowball import models

stocks = models.Stock.objects.all()
print 'total:', stocks.count()
for stock in stocks:
    models.Log.objects.create(
        stock=stock,
        count=stock.count,
        weight=stock.weight,
        weight_in=stock.weight_in,
        weight_out=stock.weight_out,
        earnings=stock.earnings
    )
    print stock.id
