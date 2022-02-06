from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import About
from profiles.forms import AboutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings


@login_required
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
def about_add(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Create About Information')
            return redirect('admin-about-list')
    else:   
        form = AboutForm()
    context = {
        'form': form, 'title': 'Aumenta Informasaun About Us'
    }
    return render(request, 'profiles/about_form.html', context)
  
@login_required
def about_update(request, hashid):
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
      'form': form, 'title': 'Aumenta Informasaun About Us'
  }
  return render(request, 'profiles/about_form.html', context)

@login_required
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