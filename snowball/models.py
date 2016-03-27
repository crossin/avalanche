from django.db import models

class Stock(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    count = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    weight_in = models.FloatField(default=0)
    weight_out = models.FloatField(default=0)
    earnings = models.FloatField(default=0)

    def __unicode__(self):
        return self.code + self.name

class Portfolio(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    earnings = models.FloatField(default=0)

    def __unicode__(self):
        return self.code + self.name

class Position(models.Model):
    stock = models.ForeignKey(Stock, related_name='portfolios')
    portfolio = models.ForeignKey(Portfolio, related_name='stocks')
    weight = models.FloatField(default=0)


class Log(models.Model):
    stock = models.ForeignKey(Stock, related_name='logs')
    count = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    weight_in = models.FloatField(default=0)
    weight_out = models.FloatField(default=0)
    earnings = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)


class KLine(models.Model):
    stock = models.ForeignKey(Stock, related_name='kline')
    date = models.DateField()
    price_last = models.FloatField(default=0)
    price_open = models.FloatField(default=0)
    price_close = models.FloatField(default=0)
    price_max = models.FloatField(default=0)
    price_min = models.FloatField(default=0)
    volume = models.IntegerField(default=0)
    turnover = models.IntegerField(default=0)

