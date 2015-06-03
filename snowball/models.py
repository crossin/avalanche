from django.db import models

class Stock(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    count = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    earnings = models.FloatField(default=0)

    def __unicode__(self):
        return self.code + self.name

class Portfolio(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=16)

    def __unicode__(self):
        return self.code + self.name

class Position(models.Model):
    stock = models.ForeignKey(Stock, related_name='portfolios')
    portfolio = models.ForeignKey(Portfolio, related_name='stocks')
