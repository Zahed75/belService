from django.db import models

# Create your models here.


class ProductImage(models.Model):
    ImageUrl = models.ImageField(upload_to='images/')
    ImageName = models.CharField(max_length=50,blank=True,null=True)
    ImageDescription = models.CharField(max_length=50,blank=True,null=True)


    def __str__(self):
        return self.ImageName




