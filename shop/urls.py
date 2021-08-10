from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name = 'about'),
    path('addProduct/',add_product,name = 'about'),
    path('postcategories/',post_Categories,name = 'about'),
    path('postproduct/',post_Product,name = 'about'),
    path('<str:category_id>/',category,name = 'category_id'),
    path('<int:id>/',product_by_id,name = 'id'),

]