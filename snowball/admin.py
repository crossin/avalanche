from django.contrib import admin
from snowball import models

class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock', 'portfolio']

admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.Portfolio, PortfolioAdmin)
admin.site.register(models.Position, PositionAdmin)
