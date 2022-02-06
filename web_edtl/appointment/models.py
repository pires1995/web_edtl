from django.db import models
import hashlib
from main.models import User

class AppointmentTo(models.Model):
    name = models.CharField(max_length=250)
    name_to = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

class Appointment(models.Model):
    appointment_to = models.ForeignKey(AppointmentTo, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=254, null=False)
    last_name = models.CharField(max_length=254, null=True)
    email = models.CharField(max_length=254, null=True)
    mobile = models.IntegerField(null=True,blank=False)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True)
    approved_date = models.DateTimeField(auto_now_add=True, null=True)
    approved_comment = models.TextField(null=True, blank=True)
    is_reject = models.BooleanField(default=False, null=True, blank=True)
    reject_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    reject_comment = models.TextField(null=True, blank=True)
    reply_date = models.DateTimeField(auto_now_add=True, null=True)
    reply_comment = models.TextField(null=True, blank=True)
    is_cancelled = models.BooleanField(default=False, null=True)
    is_done = models.BooleanField(default=False, null=True)
    done_date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.first_name} {0.appointment_date}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Appointment, self).save(*args, **kwargs)