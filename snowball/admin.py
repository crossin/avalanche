from django.contrib import admin
from snowball import models, fetchk

class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'weight', 'earnings', 'count', 'weight_in', 'weight_out']
    search_fields = ['code', 'name']
    actions = ['fetch_kline']

    def fetch_kline(self, request, queryset):
        stocks = queryset.all()
        for stock in stocks:
            if fetchk.fetch(stock):
                self.message_user(request, 'success')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'earnings']

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock', 'portfolio', 'weight']

class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock', 'weight', 'earnings', 'count', 'weight_in', 'weight_out', 'date']

class KLineAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock', 'date','price_last', 'price_open', 'price_close', 'price_max', 'price_min',
     'volume', 'turnover']


admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.Portfolio, PortfolioAdmin)
admin.site.register(models.Position, PositionAdmin)
admin.site.register(models.Log, LogAdmin)
admin.site.register(models.KLine, KLineAdmin)
