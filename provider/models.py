from django.db import models

# Create your models here.


class HomeFeature(models.Model):
    featureName = models.CharField(max_length=222,blank=True,null=True)
    coverImage=models.ImageField(upload_to='cover')

    def __str__(self):
        return self.featureName




class Product(models.Model):
    productId = models.CharField(max_length=255, unique=True)
    featureImage = models.ImageField(upload_to='feature_images/')
    productImages = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.productId

