from django.urls import path
from .views import *




urlpatterns = [

path('api/upload-images/', upload_multiple_images,),

]