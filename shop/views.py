from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .connect import *
from .forms import *
def index(request):
    cats = Categories.objects.all()
    product = Products.objects.all()
    context = {
        'cats':cats,
        'products':product
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse('bu about')

def add_product(request):
    form = AddProduct()
    product_name = request.POST.get('product_name')
    price = request.POST.get('price')
    category_id = request.POST.get('category_id')
    product_image = request.POST.get('product_image')
    form = AddProduct(request.POST,request.FILES)
    if form.is_valid():
           print('Saqlandi')
           new = Products(product_name = product_name, price = price, category_id = category_id, product_image = product_image)
           new.save()
    else:
        print('Saqlanmadi')
    # form.product_name, form.price, form.category_id =product_name, price, category_id
    print(form)
    context = {
        'form':form,
    }
    return render(request, 'addProduct.html', context)
def post_Categories(request):
    form = PostProduct()
    form = PostProduct(request.POST,request.FILES)
    if form.is_valid():
           print('Saqlandi')
           form.save()
    else:
        print('Saqlanmadi')
    form1 = PostCategories()
    form1 = PostCategories(request.POST,request.FILES)
    if form1.is_valid():
           print('Saqlandi')
           form1.save()
    else:
        print('Saqlanmadi')
    cats = Categories.objects.all()
    # form.product_name, form.price, form.category_id =product_name, price, category_id
    print(form1)
    context = {
        'form':form,
        'form1':form1,
        'cats':cats,
    }
    return render(request, 'addProduct.html', context)
def post_Product(request):
    form = PostProduct()
    form = PostProduct(request.POST,request.FILES)
    if form.is_valid():
           print('Saqlandi')
           form.save()
    else:
        print('Saqlanmadi')
    form1 = PostCategories()
    form1 = PostCategories(request.POST,request.FILES)
    if form1.is_valid():
           print('Saqlandi')
           form1.save()
    else:
        print('Saqlanmadi')
    prs = Products.objects.all()
    # form.product_name, form.price, form.category_id =product_name, price, category_id
    print(form1)
    context = {
        'form':form,
        'form1':form1,
        'prs':prs,
    }
    return render(request, 'products.html', context)

def category(request,category_id):
    cats = Categories.objects.all()
    product = Products.objects.filter(id=int(category_id))
    context = {
        'cats':cats,
        'products':product
    }
    return render(request,'one_product.html',context)
def product_by_id(request,product_id):
    cats = Categories.objects.all()
    product = Products.objects.filter(id = int(product_id))
    print(product)
    context = {
        'cats':cats,
        'products':product
    }
    return render(request,'index.html',context)