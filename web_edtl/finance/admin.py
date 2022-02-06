from django.contrib import admin
from finance.models import Client, Bill
# Register your models here.

admin.site.register(Client)
admin.site.register(Bill)
