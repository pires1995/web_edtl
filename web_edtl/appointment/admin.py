from django.contrib import admin
from appointment.models import Appointment, AppointmentTo, Position, Municipality, ContactMunicipality, Suggestion
# Register your models here.

admin.site.register(Appointment)
admin.site.register(AppointmentTo)
admin.site.register(Position)
admin.site.register(Municipality)
admin.site.register(ContactMunicipality)
admin.site.register(Suggestion)
