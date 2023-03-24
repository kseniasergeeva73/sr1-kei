from django.shortcuts import render
from .models import Product, Detail, Customer


def index(request):
    return render(request, "index.html")


def product(request):
    products = Product.objects.order_by(' product_name')

    return render(request, ' product.html', {'products': products})


def detail(request):
    details = Detail.objects.order_by(' product_name')

    return render(request, ' detail.html', {'details': details})


def customer(request):
    customers = Customer.objects.order_by('product_name')

    return render(request, 'customer.html', {'customers': customers})

# Create your views here.
