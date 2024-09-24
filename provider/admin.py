from django.contrib import admin
from.models import *



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id','ImageName']