from django.db import models
from django.contrib.auth.models import User

class Profile():
    pass
class Categories(models.Model):
    category_name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=200,null=True)
    added_time = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    title = models.CharField(max_length=100,null=True)
class Products(models.Model):
    product_name = models.CharField(max_length=100,null=True)
    product_image = models.ImageField(null=True)
    price = models.FloatField(null=True)
    category_id = models.FloatField()
    @property
    def imageUrl(self):
        try:
            return self.product_image.url
        except Exception as exp:
            return exp


