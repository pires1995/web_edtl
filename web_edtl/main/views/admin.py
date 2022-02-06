from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    group = request.user.groups.all()[0].name
    context = {
        'group': group, 'title': 'Dashboard'
    }
    return render(request, 'web_admin/home.html', context)
