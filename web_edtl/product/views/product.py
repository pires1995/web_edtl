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
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def product_list(request):
    group = request.user.groups.all()[0].name
    objects = Product.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Produto', 'group':group
    }
    return render(request, 'product/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def product_add(request):
    group = request.user.groups.all()[0].name
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
        'title': 'Aumenta Produto', 'group':group, 'subtitle': 'Produto', 'form': form
    }
    return render(request, 'product/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def product_update(request, hashid):
    group = request.user.groups.all()[0].name
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
        'title': 'Altera Produto', 'group':group, 'subtitle': 'Produto', 'form': form
    }
    return render(request, 'product/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def product_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Product, hashed=hashid)
    context = {
        'title': 'Detail Product', 'group':group, 'subtitle': 'Product', 'objects': objects
    }
    return render(request, 'product/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def product_activate(request, hashid):
    objects = get_object_or_404(Product, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Product')
    return redirect('admin-product-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def product_deactivate(request, hashid):
    objects = get_object_or_404(Product, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Product')
    return redirect('admin-product-list')