from django.db import models

# Create your models here.


class HomeFeature(models.Model):
    featureName = models.CharField(max_length=222,blank=True,null=True)
    coverImage=models.ImageField(upload_to='cover')

    def __str__(self):
        return self.featureName
