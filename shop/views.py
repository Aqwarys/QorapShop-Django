from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home_page(request):
    categories = Category.objects.filter(is_sub=False)[:10]
    context = {
        'categories': categories
    }
    return render(request, 'shop/home.html',context=context)

def catefory_page(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }

    return render(request, 'shop/category.html', context=context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context=context)
