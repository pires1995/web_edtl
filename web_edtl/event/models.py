from django.db import models
import hashlib
from .utils import path_and_rename_event
from main.models import User

class Event(models.Model):
    model_name = "Event"
    name_tet = models.CharField(max_length=254, null=False)
    name_por = models.CharField(max_length=254, null=True)
    name_eng = models.CharField(max_length=254, null=True)
    overview_tet = models.TextField(null=True, blank=True)
    overview_por = models.TextField(null=True, blank=True)
    overview_eng = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_event, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    is_send_notif = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.name_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Event, self).save(*args, **kwargs)