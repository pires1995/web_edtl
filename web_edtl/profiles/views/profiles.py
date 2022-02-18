from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import About, Service
from profiles.forms import AboutForm, ServiceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def about_list(request):
  group = request.user.groups.all()[0].name
  objects = About.objects.first()
  context = {
    'group': group,
    'objects': objects,
    'title': 'About EDTL', 'legend': 'About EDTL'
  }
  return render(request, 'profiles/about_list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def about_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Create About Information')
            return redirect('admin-about-list')
    else:   
        form = AboutForm()
    context = {
        'form': form, 'group':group, 'title': 'Aumenta Informasaun About Us'
    }
    return render(request, 'profiles/about_form.html', context)
  
@login_required
@allowed_users(allowed_roles=['admin','media'])
def about_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(About, hashed=hashid)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Update About Information')
            return redirect('admin-about-list')
    else:   
        form = AboutForm(instance=objects)
    context = {
        'form': form, 'group':group, 'title': 'Aumenta Informasaun About Us'
    }
    return render(request, 'profiles/about_form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def view_pdf(request, hashid):
    objects = get_object_or_404(About, hashed=hashid)
    file = str(settings.BASE_DIR)+str(objects.org_chart.url)
    # file = objects.file.url
    try:
        if file:
            return FileResponse(open(file, 'rb'), content_type='application/pdf')
        else:
            return FileResponse(open(file, 'rb'))
    except FileNotFoundError:
        raise Http404('not found')


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def service_list(request):
  group = request.user.groups.all()[0].name
  objects = Service.objects.all()
  context = {
    'group': group,
    'objects': objects,
    'title': 'Service EDTL', 'legend': 'Service EDTL'
  }
  return render(request, 'profiles/service_list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def service_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Create Service Information')
            return redirect('admin-service-list')
    else:   
        form = ServiceForm()
    context = {
        'form': form, 'group':group, 'title': 'Aumenta Informasaun Service Us'
    }
    return render(request, 'profiles/service_form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def service_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Service, hashed=hashid)
    context = {
        'title': 'Detail Service','group':group, 'subtitle': 'Service', 'objects': objects
    }
    return render(request, 'profiles/service_detail.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def service_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Service, hashed=hashid)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Update Service Information')
            return redirect('admin-service-list')
    else:   
        form = ServiceForm(instance=objects)
    context = {
        'form': form, 'group':group, 'title': 'Aumenta Informasaun Service Us'
    }
    return render(request, 'profiles/service_form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def service_activate(request, hashid):
    objects = get_object_or_404(Service, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Service')
    return redirect('admin-service-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def service_deactivate(request, hashid):
    objects = get_object_or_404(Service, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Service')
    return redirect('admin-service-list')
