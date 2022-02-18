from django.shortcuts import render, redirect, get_object_or_404
from appointment.models import ContactMunicipality
from appointment.forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def contact_list(request):
    group = request.user.groups.all()[0].name
    objects = ContactMunicipality.objects.all()
    context = {
        'objects': objects,'group': group, 'title': 'Lista Kontaktu Munisipiu'
    }
    return render(request, 'contact/list.html',context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def contact_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(ContactMunicipality)
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Contact')
            return redirect('admin-contact-list')
    else:
        form = ContactForm()
    context = {
        'title': 'Aumenta Kontaktu Municipio','group': group,'subtitle': 'Contact', 'form': form
    }
    return render(request, 'contact/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def contact_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(ContactMunicipality, hashed=hashid)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Contact')
            return redirect('admin-contact-list')
    else:
        form = ContactForm(instance=objects)
    context = {
        'title': 'Altera Kontaktu Munisipiu','group': group,'subtitle': 'Contact', 'form': form
    }
    return render(request, 'contact/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def contact_activate(request, hashid):
    objects = get_object_or_404(ContactMunicipality, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Contact')
    return redirect('admin-contact-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def contact_deactivate(request, hashid):
    objects = get_object_or_404(ContactMunicipality, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Contact')
    return redirect('admin-contact-list')