import urllib2
import json
import time
import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='avalanche.settings'
django.setup()

from snowball import models


def get_html(url):
    send_headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive',
        'Host':'xueqiu.com',
        'Cookie':r's=iadygnff.g98ms6; xq_a_token=7e06ebb83c8d925cb776b5eb4fe87b09369d7c6e; xq_r_token=f90b576a98f834873eae35246026eff163237a0a; __utma=1.277142738.1433166723.1433166839.1433258555.4; __utmb=1.3.10.1433258555; __utmc=1; __utmz=1.1433166723.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E9%9B%AA%E7%90%83; Hm_lvt_1db88642e346389874251b5a1eded6e3=1433166723,1433258555; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1433258610',
    }
    req = urllib2.Request(url, headers=send_headers)
    resp = urllib2.urlopen(req)
    html = resp.read()
    return html    

def fetch_portfolio(code):
    url = 'http://xueqiu.com/p/' + code
    html = get_html(url)

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
        stock.count += 1
        stock.save()
        # add position
        models.Position.objects.get_or_create(portfolio=portfolio, stock=stock)

def get_portfolio_list(page):
    url = 'http://xueqiu.com/cubes/discover/rank/cube/list.json?category=10&count=10&market=cn&page=%d' % page
    html = get_html(url)
    dic = json.loads(html)
    for p in dic['list']:
        portfolio = models.Portfolio.objects.get_or_create(code=p['symbol'], name=p['name'])

# test fetch
# for page in xrange(1, 42):
#     print 'fetch page', page
#     get_portfolio_list(page)
#     time.sleep(2)

portfolios = models.Portfolio.objects.all()
for p in portfolios:
    print p.id, p.name
    fetch_portfolio(p.code)
    time.sleep(2)

