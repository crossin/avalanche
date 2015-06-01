import urllib2
import json
import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='avalanche.settings'
django.setup()

from snowball import models


def fetch_portfolio(code):
    url = 'http://xueqiu.com/p/' + code
    send_headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive'
    }

    req = urllib2.Request(url, headers=send_headers)
    resp = urllib2.urlopen(req)
    html = resp.read()

    pos_start = html.find('SNB.cubeInfo = ') + 15
    pos_end = html.find('SNB.cubePieData')
    data = html[pos_start:pos_end]
    dic = json.loads(data)

    # add Portfolio
    portfolio, c = models.Portfolio.objects.get_or_create(code=dic['symbol'], name=dic['name'])
    # add Stock
    stocks = dic['view_rebalancing']['holdings']
    for s in stocks:
        stock, c = models.Stock.objects.get_or_create(code=s['stock_symbol'], name=s['stock_name'])
        # add position
        models.Position.objects.get_or_create(portfolio=portfolio, stock=stock)


# test fetch
lst_port = ['ZH016180', 'ZH002820', 'ZH014837', 'ZH299079', 'ZH346858', 'ZH107143', 'ZH132008', 'ZH228246', 'ZH145957']
for p in lst_port:
    fetch_portfolio(p)

