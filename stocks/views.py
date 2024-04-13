from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from stocks.services.query_service import query_service
from django.http import JsonResponse
import traceback

class PlaceTrade(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user_id = self.request.data['user_id']
            trade_type = self.request.data['trade_type']
            stock_id = self.request.data['stock_id']
            quantity = self.request.data['quantity']
            query_service.place_trade(user_id,trade_type,stock_id,quantity)

            return Response("Success", status=200)
        except Exception:
            traceback.print_exc()
            return Response({'Error':'Something went wrong.'}, status=400)

class TotalValue(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user_id = self.request.data['user_id']
            trade_type = self.request.data['trade_type']
            stock_id = self.request.data['stock_id']
            total_order = query_service.get_total_order(user_id,stock_id,trade_type)
            stock_price = list(query_service.get_stock_price(stock_id))
            total_value = int(total_order['quantity__sum']) * float(stock_price[0]['price'])

            result = {
                "user_id":user_id,
                "stock_id": stock_id,
                "stock_price": stock_price[0]['price'],
                "total_order": total_order['quantity__sum'],
                "total_value": total_value
            }

            return JsonResponse(result, status=200)
        except Exception:
            traceback.print_exc()
            return Response({'Error':'Something went wrong.'}, status=400)
        