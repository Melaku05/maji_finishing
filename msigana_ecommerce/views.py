from django.shortcuts import render
from slideshow.models import BackgroundSlide
from store.models import Product
from users.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import os

def home(request):
    products = Product.objects.all().filter(product_is_available=True)
    products = Product.objects.filter(product_is_available=True).order_by('-product_modified_date', '-product_created_date')
    slides = BackgroundSlide.objects.filter(is_active=True)
    context = {
        'products': products,
        'slides': slides
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about-us.html')

def minerals(request):
    return render(request, 'minerals.html')
def new_arrivals(request):
    products = Product.objects.all().filter(product_is_available=True)
    context = {
        'products': products
    }
    return render(request, 'new-arrivals.html', context)

def online_order(request):
    products = Product.objects.all().filter(product_is_available=True)
    context = {
        'products': products
    }
    return render(request, 'online_order.html', context)
