from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Qoute
class getAllExistingQoutes(APIView):

	def get(self, request):
		qoutes = Qoute.objects.all()
		response = {
            'status_code':status.HTTP_200_OK,
            'body': qoutes
		}
		return Response(response)

class getSpecificQoutes(APIView):

	def post(self, request):
		qoutes = Qoute.objects.get(id=request.data.get('id'))
		response = {
            'status_code':status.HTTP_200_OK,
            'body': qoutes
		}
		return Response(response)

class createNewQoutes(APIView):

	def post(self, request):
		qoutes = Qoute.objects.create(author=request.data.get('author'),
        quote = request.data.get('qoute'))
		response = {
            'status_code':status.HTTP_200_OK,
            'body': qoutes
		}
		return Response(response)

class UpdateExistingQoutes(APIView):

	def put(self, request):
		qoutes = Qoute.objects.filter(id = request.data.get('id')).update(author=request.data.get('author'),
        quote = request.data.get('qoute'))
		response = {
            'status_code':status.HTTP_200_OK,
            'body': qoutes
		}
		return Response(response)

class DeleteExistingQoutes(APIView):

	def delete(self, request):
		qoutes = Qoute.objects.filter(id = request.data.get('id')).delete()
		response = {
            'status_code':status.HTTP_200_OK,
            'body': qoutes
		}
		return Response(response)
