from django.urls import path
from stocks.api import *
urlpatterns = [
	#Exam api live coding
	path('get-all-qoutes/', getAllExistingQoutes.as_view()),
	path('get-specific-qoutes/', getSpecificQoutes.as_view()),
    path('create-qoutes/', createNewQoutes.as_view()),
	path('update-specific-qoutes/', UpdateExistingQoutes.as_view()),
    path('delete-qoutes/', DeleteExistingQoutes.as_view()),	
]