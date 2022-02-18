from django.db import models
from .utils import path_and_rename_bill
import hashlib
from main.models import User

class Client(models.Model):
    name = models.CharField(max_length=250, null=True)
    numero_kontador = models.PositiveBigIntegerField()
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250, null=True, blank=True)
    temp_password = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Client, self).save(*args, **kwargs)

class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bill_number=models.CharField(max_length=500,null=True)
    payment_date = models.DateField(null=True)
    file = models.ImageField(default='default.jpg', upload_to=path_and_rename_bill, null=True, blank=True)
    upload_date = models.DateField(null=True)
    is_done = models.BooleanField(default=False, null=True)
    done_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    done_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.bill_number} - {0.client}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Bill, self).save(*args, **kwargs)
