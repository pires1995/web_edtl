from django.contrib import admin
from custom.models import Municipality, AdministrativePost, Village, Year

# Register your models here.
admin.site.register(Municipality)
admin.site.register(AdministrativePost)
admin.site.register(Village)
admin.site.register(Year)