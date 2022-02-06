from django.shortcuts import render, redirect, get_object_or_404
from appointment.models import Appointment
from appointment.forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from datetime import datetime

@login_required
def appointment_list(request):
    objects = Appointment.objects.filter(is_approved=False, is_reject=False)
    if request.method == 'POST':
        id = request.POST.get('id')
        decision = request.POST.get('decision')
        comments = request.POST.get('comments')
        obj = Appointment.objects.get(pk=id)
        if decision == "1":
            obj.is_approved = True
            obj.approved_comment = comments
            obj.approved_date = datetime.now()
            obj.is_reject = False
            obj.reject_date = None
            obj.reject_comment = ''
        elif decision == "2":
            obj.is_reject = True
            obj.is_approved = False
            obj.reject_comment = comments
            obj.approved_comment = ''
            obj.approved_date = None
            obj.reject_date = datetime.now()
        else:
            obj.is_reject = False
            obj.is_approved = False
            obj.reply_comment = comments
            obj.approved_date = None
            obj.reject_date = None
            obj.reply_date = datetime.now()
        obj.user = request.user
        obj.save()
        messages.success(request, f'Successfully Send Messages')
        return redirect('admin-appointment-list')
    context = {
        'objects': objects, 'title': 'Lista Appointment'
    }
    return render(request, 'appointment/list.html',context)



@login_required
def appointment_approved_list(request):
    objects = Appointment.objects.filter(is_approved=True, is_done=False, is_cancelled=False).order_by('-approved_date')
    done = Appointment.objects.filter(is_approved=True, is_done=True).order_by('-done_date')
    not_done = Appointment.objects.filter(is_approved=True, is_done=False,  is_cancelled=True)
    context = {
        'objects': objects, 'title': 'List Approved Appointment ', 'done': 'Done Appointment', 'not_done': 'Cancel Appointment',\
            'done_list': done, 'not_done_list': not_done
    }
    return render(request, 'appointment/appointment_approved.html',context)

@login_required
def appointment_reject_list(request):
    objects = Appointment.objects.filter(is_approved=False, is_reject=True).order_by('-reject_date')
    context = {
        'objects': objects, 'title': 'List Reject Appointment '
    }
    return render(request, 'appointment/appointment_reject.html',context)

@login_required
def appointment_approved_done(request, hashid):
    objects = get_object_or_404(Appointment, hashed=hashid)
    objects.is_done = True
    objects.done_date = datetime.now()
    objects.save()
    messages.success(request, f'Successfully Set Status to Done')
    return redirect('admin-appointment-approved-list')

@login_required
def appointment_approved_not_done(request, hashid):
    objects = get_object_or_404(Appointment, hashed=hashid)
    objects.is_approved =True
    objects.is_done = False
    objects.is_cancelled = True
    objects.save()
    messages.success(request, f'Successfully Set Status to Cancelled')
    return redirect('admin-appointment-approved-list')


@login_required
def appointment_detail(request, hashid):
    objects = get_object_or_404(Appointment, hashed=hashid)
    context = {
        'title': 'Detail Appointment', 'subtitle': 'Appointment', 'objects': objects
    }
    return render(request, 'appointment/detail.html', context)


