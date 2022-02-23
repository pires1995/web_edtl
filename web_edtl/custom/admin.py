from django.contrib import admin
from custom.models import Municipality, AdministrativePost, Village, Year, FirebaseToken, IpModel

# Register your models here.
admin.site.register(Municipality)
admin.site.register(AdministrativePost)
admin.site.register(Village)
admin.site.register(Year)
admin.site.register(FirebaseToken)
admin.site.register(IpModel)
