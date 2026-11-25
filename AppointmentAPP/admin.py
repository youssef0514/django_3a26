from django.contrib import admin

from .models import Appointment


@admin.action(description="make them confirmed")
def confirmed(model, request, queryset):
    queryset.update(status="confirmed")

@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    list_display=("reason","status","duration_minutes","appointment_date")
    list_filter=("status","appointment_date")
    list_editable=("status",)
    serach_fields=("reason","status")
    ordering=("-appointment_date",)
    fieldsets=(
        ('Description', {
            
            'fields': ('reason', 'prescription', 'status')
        }),
        ('Date +Duration', {
            'fields': ('appointment_date',)
        }),
        ('Relations', {
            'fields': ('doctor', 'patient')
        }),
        ("Planification", {
            'fields': ("created_at", "updated_at")
        })
    )
    readonly_fields = ("created_at", "updated_at")