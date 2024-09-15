import code

from django.shortcuts import render
from .modules import *

# Create your views here.



@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_feature(request):
    try:
        payload = request.data
        data_serializer = HomeFeatureSerializer(data=payload,context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': "Product added successfully",
                'data': data_serializer.data,
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "Invalid data",
                'errors': data_serializer.errors,
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_all_feature(request):
    try:

        features = HomeFeature.objects.all()
        data_serializer = HomeFeatureSerializer(features, many=True)

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Get All Features Fetched Successfully',
            'data': data_serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })



@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def add_product_picture(request):
    try:
        payload = request.data
        data_serializer = ProductSerializer(data=payload,context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
               'code': status.HTTP_200_OK,
                'message': "Product Picture successfully",
                'data': data_serializer.data,
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "Invalid data",
                'errors': data_serializer.errors,
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })




@api_view(['GET'])
def get_all_product_picture(request):
    try:
        products = Product.objects.all()
        data_serializer = ProductSerializer(products, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': "Product Picture Get successfully",
            'data': data_serializer.data,
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })



