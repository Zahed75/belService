from django.urls import path
from .views import *

urlpatterns = [

    path('api/upload-images/', upload_multiple_images),
    path('api/get-all-images/', get_all_images),
    path('api/invoice/', index),
    path('order/create/', create_order_and_send_invoice, name='create_order'),

]
