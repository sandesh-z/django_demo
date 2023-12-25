from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import FirstSerializer
from .models import FirstModel

# create a viewset


class FirstViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = FirstModel.objects.all()

	# specify serializer to be used
	serializer_class = FirstSerializer
