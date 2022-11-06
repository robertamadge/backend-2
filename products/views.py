from django.shortcuts import render
from django.contrib import messages

from products.forms import ProductForm
from products.models import Product

def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product registered with success')
    else:
        form = ProductForm()
    return render(request, 'form_products.html', {'form': form})

def details_products(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'list_product.html', {'product': product})