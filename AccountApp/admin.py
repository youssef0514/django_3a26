from django.contrib import admin
from .models import*
from AppointmentAPP.models import Appointment
# Register your models here.
admin.site.register(User)
admin.site.register(Patient)

class AppointmentStacked(admin,TabularInline):
    model=Appointment
    extra=1
class DoctorPersoClass(admin.ModelAdmin):
    inlines=[AppointmentStacked]
admin.site.register(Doctor,DoctorPersoClass)


admin.site.register(Speciality)

