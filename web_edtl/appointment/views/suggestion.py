from django.shortcuts import render, redirect, get_object_or_404
from appointment.models import Suggestion
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def suggestion_list(request):
    objects = Suggestion.objects.all()
    context = {
        'objects': objects, 'title': 'List Suggestion'
    }
    return render(request, 'suggestion/list.html',context)


@login_required
def suggestion_detail(request, hashid):
    objects = get_object_or_404(Suggestion, hashed=hashid)
    context = {
        'title': 'Detail Suggestion', 'subtitle': 'Suggestion', 'objects': objects
    }
    return render(request, 'suggestion/detail.html', context)
