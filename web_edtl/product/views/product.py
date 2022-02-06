from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from product.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from datetime import date

@login_required
def product_list(request):
    objects = Product.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Produto',
    }
    return render(request, 'product/list.html', context)

@login_required
def product_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Product)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Product')
            return redirect('admin-product-list')
    else:
        form = ProductForm()
    context = {
        'title': 'Aumenta Produto','subtitle': 'Produto', 'form': form
    }
    return render(request, 'product/form.html', context)

@login_required
def product_update(request, hashid):
    objects = get_object_or_404(Product, hashed=hashid)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Product')
            return redirect('admin-product-list')
    else:
        form = ProductForm(instance=objects)
    context = {
        'title': 'Altera Produto','subtitle': 'Produto', 'form': form
    }
    return render(request, 'product/form.html', context)

@login_required
def product_detail(request, hashid):
    objects = get_object_or_404(Product, hashed=hashid)
    context = {
        'title': 'Detail Product', 'subtitle': 'Product', 'objects': objects
    }
    return render(request, 'product/detail.html', context)