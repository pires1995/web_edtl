from django.shortcuts import render, redirect, get_object_or_404
from appointment.models import Suggestion
from django.contrib.auth.decorators import login_required
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def suggestion_list(request):
    group = request.user.groups.all()[0].name
    objects = Suggestion.objects.all()
    context = {
        'objects': objects,'group': group, 'title': 'List Suggestion'
    }
    return render(request, 'suggestion/list.html',context)


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def suggestion_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Suggestion, hashed=hashid)
    context = {
        'title': 'Detail Suggestion','group': group, 'subtitle': 'Suggestion', 'objects': objects
    }
    return render(request, 'suggestion/detail.html', context)
