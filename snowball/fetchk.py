import urllib
import datetime
from snowball import models

def fetch(stock):
    code = str(stock.code)
    if code.startswith('SH'):
        zone = 1
    elif code.startswith('SZ'):
        zone = 2
    else:
        print 'error'
        return False
    code = code[2:]
    url = r'http://flashquote.stock.hexun.com/Quotejs/DA/%d_%s_DA.html?start=201601010000' % (zone, code)
    # print url
    req = urllib.urlopen(url)
    data = req.read()
    dataset = data[36:-5].split('],[')
    if len(dataset) < 3:
        return False
    print len(dataset)
    klines = []
    last = 0
    factor = 1
    for d in dataset:
        value = d.split(',')
        date = datetime.datetime.strptime(value[0], '%Y%m%d')
        kline = models.KLine()
        kline.stock = stock
        kline.date = date
        if last != 0 and float(value[1]) * factor != last:
            factor *= (last / (float(value[1]) * factor))
        kline.price_last = float(value[1]) * factor
        kline.price_open = float(value[2]) * factor
        kline.price_max = float(value[3]) * factor
        kline.price_min = float(value[4]) * factor
        kline.price_close = float(value[5]) * factor
        kline.volume = int(value[6])
        kline.turnover = int(value[7])
        klines.append(kline)
        last = kline.price_close
    models.KLine.objects.filter(stock=stock).delete()
    models.KLine.objects.bulk_create(klines)
    return True
