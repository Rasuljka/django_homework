from django.shortcuts import render, get_object_or_404

from .models import *


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def products(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'catalog/products.html', context)


def product_detail(request, pk):
    context = {'product_detail': get_object_or_404(Product, pk=pk)}
    return render(request, 'catalog/product_detail.html', context)
