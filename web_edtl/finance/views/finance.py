from django.shortcuts import render, redirect, get_object_or_404
from finance.models import Bill
from finance.utils import getid
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
import re
from main.models import User
from datetime import datetime

@login_required
def bill_list(request):
    bills = Bill.objects.filter(is_done=False)
    bills_approved = Bill.objects.filter(is_done=True)
    # usergroup = request.user.groups.all()[0].name
    context = {
        'bills': bills, 'title': 'Request Bill List', 'bills_approved': bills_approved
    }
    return render(request, 'finance/list.html', context)

@login_required
def bill_detail(request, hashid):
    objects = get_object_or_404(Bill, hashed=hashid)
    context = {
        'title': 'Detail Bill', 'subtitle': 'Bill', 'objects': objects
    }
    return render(request, 'finance/detail.html', context)

@login_required
def bill_approve(request, hashid):
    objects = get_object_or_404(Bill, hashed=hashid)
    objects.is_done = True
    objects.done_by = request.user
    objects.done_date = datetime.now()
    objects.save()
    messages.success(request, 'Successfully Approve Bill')
    return redirect('admin-bill-detail', hashid=hashid)