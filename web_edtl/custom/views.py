import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AdministrativePost, Village
from main.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy
from custom.forms import UserUpdateForm
def load_posts(request):
	mun_id = request.GET.get('municipality')
	posts = AdministrativePost.objects.filter(municipality_id=mun_id).order_by('name')
	return render(request, 'custom/posts_dropdown.html', {'posts': posts})

def load_villages(request):
	post_id = request.GET.get('post')
	villages = Village.objects.filter(administrativepost_id=post_id).order_by('name')
	return render(request, 'custom/villages_dropdown.html', {'villages': villages})

@login_required
def ProfileUpdate(request):
	user = User.objects.get(pk=request.user.pk)
	group = request.user.groups.all()[0].name
	# objects = Employee.objects.get(pk=user.employee.id)
	# empposition = EmployeePosition.objects.filter(employee=objects).first()
	# empdivision = EmployeeDivision.objects.filter(employee=objects).first()
	
	context = {
		# 'objects': objects, 'empposition': empposition, 'empdivision': empdivision,
		'group': group, 'user':user,
		'title': 'PROFILE', 'legend': 'PROFILE',
	}
	return render(request, 'auth/profile.html', context)

# Create your views here.
@login_required
def AccountUpdate(request):
	group = request.user.groups.all()[0].name
	objects = User.objects.get(pk=request.user.pk)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('user-account')
	else:
		u_form = UserUpdateForm(instance=request.user)

	context = {
		'u_form': u_form,
		'title': 'ACCOUNT INFO',
		'legend': 'ACCOUNT INFO',
		'title_page': 'Account Info',
		'group': group
	}
	return render(request, 'auth/account.html', context)

class UserPasswordChangeView(PasswordChangeView):
	template_name = 'auth/change_password.html'
	success_url = reverse_lazy('user-change-password-done')

class UserPasswordChangeDoneView(PasswordResetDoneView):
	template_name = 'auth/change_password_done.html'