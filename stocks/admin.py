from django.contrib import admin

# Register your models here.

from .models import *


class StocksAdmin(admin.ModelAdmin):
     list_display = (
        'id',
        'name',
        'price'
    )

class TradeAdmin(admin.ModelAdmin):
     list_display = (
        'id',
        'user',
        'trade_type',
        'stock',
        'quantity'
    )

class QoutesAdmin(admin.ModelAdmin):
     list_display = (
        'id',
        'author',
        'quote',
    )

admin.site.register(Stocks, StocksAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(Qoute, QoutesAdmin)