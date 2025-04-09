from django.contrib import admin
from .models import Medication, Appointment, EmergencyContact

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'schedule', 'user', 'is_active')
    list_filter = ('is_active', 'start_date')
    search_fields = ('name', 'user__username')
    date_hierarchy = 'start_date'

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'specialty', 'date', 'user')
    list_filter = ('date', 'specialty')
    search_fields = ('doctor_name', 'specialty', 'user__username')
    date_hierarchy = 'date'

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationship', 'phone', 'is_primary', 'user')
    list_filter = ('is_primary', 'relationship')
    search_fields = ('name', 'relationship', 'user__username')
