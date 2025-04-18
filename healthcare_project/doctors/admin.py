from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'specialization', 'license_number', 'years_of_experience')
    list_filter = ('specialization',)
    search_fields = ('first_name', 'last_name', 'license_number', 'email')
