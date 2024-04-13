
from stocks.models import *
from django.db.models import Sum
import json

class query_service:

	def place_trade(user_id,trade_type,stock_id,quantity):

		return Trade.objects.create(user_id = user_id, trade_type = trade_type, stock_id = stock_id, quantity = quantity)

	def get_total_order(user_id,stock_id,trade_type):

		total_order = Trade.objects.filter(user_id = user_id,stock_id = stock_id,trade_type = trade_type).aggregate(Sum('quantity'))

		return total_order
	def get_stock_price(stock_id):
		stock_price = Stocks.objects.filter(id = stock_id).values('price')

		return stock_price


		