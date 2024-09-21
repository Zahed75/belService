from django.contrib import admin
from.models import *



@admin.register(HomeFeature)

class HomeFeatureAdmin(admin.ModelAdmin):
    list_display = ('id','featureName','coverImage')






class ProductAdmin(admin.ModelAdmin):
    list_display = ('featureImage', 'productImage')


admin.site.register(Product, ProductAdmin)
