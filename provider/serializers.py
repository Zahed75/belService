from rest_framework import serializers
from .models import *



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['ImageUrl', 'ImageName', 'ImageDescription']
