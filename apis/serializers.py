# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import FirstModel
 
# Create a model serializer
class FirstSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = FirstModel
        fields = ('title', 'description')