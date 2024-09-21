from rest_framework import serializers
from .models import *



class HomeFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model= HomeFeature
        fields='__all__'







class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'