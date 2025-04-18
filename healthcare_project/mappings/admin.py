from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'assigned_date')
    search_fields = ('patient__first_name', 'doctor__last_name')
    autocomplete_fields = ['patient', 'doctor']
