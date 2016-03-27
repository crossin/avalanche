import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='avalanche.settings'
django.setup()

from snowball import models
import matplotlib.pyplot as plt

stock = models.Stock.objects.get(code='SZ000002')
history = list(stock.kline.all())
data = [k.price_close for k in history]

# show k line
plt.plot(data)
# plt.axis([0,7000,0,7000])
plt.show()