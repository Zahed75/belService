from django.urls import path
from .views import *




urlpatterns = [

    path('api/add-feature/', create_feature),
    path('api/get-all-features/',get_all_feature),
    path('api/add-product/',add_product_picture),
    path('api/get_all_pictures/',get_all_product_picture),
]