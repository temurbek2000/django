from django import forms
from .models import *
class AddProduct(forms.Form):
    product_name = forms.CharField(label = 'Mahsulot nomini kiriting:',max_length = 100,)
    price = forms.FloatField(label = 'Mahsulot narxini kiriting:')
    category_id = forms.FloatField(label = 'Mahsulot kategoriyasi id sini kiriting:')
    product_image = forms.ImageField(label='Mahsulot rasmini tanlang:')
    #
    # @property
    # def imageUrl(self):
    #     try:
    #         return self.product_image.url
    #     except Exception as exp:
    #         return exp


class PostProduct(forms.ModelForm):
    class Meta:
        model = Products
        # fields = ['product_name','price','category_id','product_image']
        fields = '__all__'

class PostCategories(forms.ModelForm):
    class Meta:
        model = Categories
        # fields = ['product_name','price','category_id','product_image']
        fields = '__all__'